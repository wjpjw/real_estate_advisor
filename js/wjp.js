queue().defer(d3.json, "./data/county.json").defer(d3.json, "./data/us-counties.json").await(makeGraphs);

/*
  history =[{price, date, stocks}, ...]
*/
function makeGraphs(error, wjp_json, county_map_json) {
    //properties
    var county=wjp_json["county"];
    var rate=wjp_json["rate"];
    var history=wjp_json["history"];
    var stocks=wjp_json["stocks"];

    //parse date
    var dateFormat = d3.time.format("%Y-%m");
    history.forEach(function(t){
      t["date"] = dateFormat.parse(t["date"]);
      t["date"].setDate(1);
    });

    //history crossfilter
    var ndx = crossfilter(history);
    var date_dim = ndx.dimension(function(d) { return d["date"]; });

    //range slider
    var minDate = date_dim.bottom(1)[0]["date"];
    var maxDate = date_dim.top(1)[0]["date"];

    //Charts
    var predictionChartDiv = dc.barChart("#prediction_chart_div");
    var usMapSvg = dc.geoChoroplethChart("#usmap_svg");
    var regionDiv = dc.numberDisplay("#region_div");

    regionDiv
	.formatNumber(d3.format("d"))
	.valueAccessor(function(d){return d;})
	.group(all);

    predictionChartDiv
	.width(600)
	.height(160)
	.margins({top: 10, right: 50, bottom: 30, left: 50})
	.dimension(dateDim)
	.group(numProjectsByDate)
	.transitionDuration(500)
	.x(d3.time.scale().domain([minDate, maxDate]))
	.elasticY(true)
	.xAxisLabel("Year")
	.yAxis().ticks(4);



    usMapSvg.width(1000)
	.height(330)
	.dimension(stateDim)
	.group(totalDonationsByState)
	.colors(["#E2F2FF", "#C4E4FF", "#9ED2FF", "#81C5FF", "#6BBAFF", "#51AEFF", "#36A2FF", "#1E96FF", "#0089FF", "#0061B5"])
	.colorDomain([0, max_state])
	.overlayGeoJson(county_map_json["features"], "state", function (d) {
	    return d.properties.name;
	})
	.projection(d3.geo.albersUsa()
    		    .scale(600)
    		    .translate([340, 150]))
	.title(function (p) {
	    return "State: " + p["key"]
		+ "\n"
		+ "Total Donations: " + Math.round(p["value"]) + " $";
	})

    dc.renderAll();

};
