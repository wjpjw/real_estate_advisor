queue().defer(d3.json, "https://d3js.org/us-10m.v1.json").await(us_heatmap);

function inspect(msg, object) {
    console.log(msg + JSON.stringify(object, null, 4));
}

function show_county_info(county_id) {
    queue().defer(d3.json, "/county/" + county_id).await(county_charts);
}

function clear(svg) {
    svg.selectAll("*").remove();
}

function county_charts(error, county_json) {
    var county = county_json["county"];
    var rate = county_json["rate"];
    var history = county_json["history"];
    var stocks = county_json["stocks"];
    //parse date
    var dateFormat = d3.time.format("%Y-%m");
    history.forEach(function(t) {
        t["date"] = dateFormat.parse(t["date"]);
        t["date"].setDate(1);
    });
}


function redraw_text(svg, data, func = function(d) { return d.name }) {
    svg.data(data)
        .transition()
        .duration(1000)
        .style("opacity", 0)
        .transition().duration(500)
        .style("opacity", 1)
        .text(func)
}

function us_heatmap(error, county_map_json) {
    var region_selected = [{ "id": 10, "name": "TestName" }];
    var region_svg = d3.select("#region_svg");
    var region_svg_text = region_svg.append('text')
        .data(region_selected)
        .attr('x', 100)
        .attr('y', 60)
        .attr('fill', '#000')
        .style("font-size", "44px")
        .classed('region_selected', true)
        .text(function(d) { return d.name })


    var heatmap_svg = d3.select("#usmap_svg");
    var heatmap_path = d3.geoPath();
    var heatmap_linearscale = d3.scaleLinear().domain([1, 10]).rangeRound([600, 860]);
    var heatmap_color = d3.scaleThreshold().domain(d3.range(3, 9)).range(d3.schemeBlues[7]);
    var heatmap_legend = heatmap_svg.append("g").attr("class", "key").attr("transform", "translate(0,40)");

    heatmap_legend.selectAll("rect")
        .data(heatmap_color.range().map(function(d) {
            d = heatmap_color.invertExtent(d);
            if (d[0] == null) d[0] = heatmap_linearscale.domain()[0];
            if (d[1] == null) d[1] = heatmap_linearscale.domain()[1];
            return d;
        }))
        .enter().append("rect")
        .attr("height", 8)
        .attr("x", function(d) { return heatmap_linearscale(d[0]); })
        .attr("width", function(d) { return heatmap_linearscale(d[1]) - heatmap_linearscale(d[0]); })
        .attr("fill", function(d) { return heatmap_color(d[0]); });

    heatmap_legend.append("text")
        .attr("class", "caption")
        .attr("x", heatmap_linearscale.range()[0])
        .attr("y", -6)
        .attr("fill", "#000")
        .attr("text-anchor", "start")
        .attr("font-weight", "bold")
        .text("");

    heatmap_legend.call(d3.axisBottom(heatmap_linearscale)
            .tickSize(13)
            .tickFormat(function(x2, i) { return i ? x2 : x2 + "/10"; })
            .tickValues(heatmap_color.domain()))
        .select(".domain")
        .remove();


    heatmap_svg.append("g")
        .attr("class", "counties")
        .selectAll("path")
        .data(topojson.feature(county_map_json, county_map_json.objects.counties).features)
        .enter().append("path")
        .attr("fill", function(d) { return heatmap_color(d.rate = d.id % 10); })
        .attr("d", heatmap_path)
        .append("title")
        .text(function(d) { return "Region ID:" + d.id + ", Rating:" + d.rate + "(/10)"; });

    heatmap_svg.append("path")
        .datum(topojson.mesh(county_map_json, county_map_json.objects.states, function(a, b) { return a !== b; }))
        .attr("class", "states")
        .attr("d", heatmap_path);


    show_county_info("01007");

}