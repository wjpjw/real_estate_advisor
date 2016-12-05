queue().defer(d3.json, "https://d3js.org/us-10m.v1.json").defer(d3.json, "http://localhost:5000/date").await(us_heatmap);

function inspect(msg, object) {
    console.log(msg + JSON.stringify(object, null, 4));
}

function clear(svg) {
    svg.selectAll("*").remove();
}

function redraw_text(svg_text, data, func) {
    svg_text.data(data)
        .transition()
        .duration(40)
        .style("opacity", 0)
        .transition().duration(20)
        .style("opacity", 1)
        .text(func)
}

function us_heatmap(error, county_map_json, all_price_json) {
    //[1] region_svg init 
    var region_selected = [{ "id": 10, "name": "---" }];
    var region_svg = d3.select("#region_svg");
    var region_svg_text = region_svg.append('text')
        .data(region_selected)
        .attr('x', 100)
        .attr('y', 60)
        .attr('fill', '#000')
        .style("font-size", "44px")
        .classed('region_selected', true)
        .text(function(d) { return d.name; });

    //[2] rating_svg init
    var rating_selected = [0];
    var rating_svg = d3.select("#rating_svg");
    var rating_svg_text = rating_svg.append('text')
        .data(rating_selected)
        .attr('x', 100)
        .attr('y', 60)
        .attr('fill', '#000')
        .style("font-size", "44px")
        .classed('rating_selected', true)
        .text(function(d) { return d; });

    //[3] usmap_svg
    var heatmap_svg_width = 960,
        heatmap_svg_height = 660,
        heatmap_svg_centered;
    var heatmap_svg = d3.select("#usmap_svg").attr("width", heatmap_svg_width).attr("height", heatmap_svg_height);

    //------------------------ Slider ------------------------
    //requires all_price_json
    var all_date_data = all_price_json["items"];

    var slider_svg = heatmap_svg,
        slider_margin = { right: 50, left: 50 },
        slider_width = +slider_svg.attr("width") - slider_margin.left - slider_margin.right,
        slider_height = +slider_svg.attr("height") + 610;

    function generate_date(index) {
        return all_date_data[index].date; //index to date
    }
    var sliderx = d3.scaleLinear()
        .domain([0, 10])
        .range([0, slider_width])
        .clamp(true);

    var slider = slider_svg.append("g")
        .attr("class", "slider")
        .attr("transform", "translate(" + slider_margin.left + "," + slider_height / 2 + ")");

    slider.append("line")
        .attr("class", "track")
        .attr("x1", sliderx.range()[0])
        .attr("x2", sliderx.range()[1])
        .select(function() { return this.parentNode.appendChild(this.cloneNode(true)); })
        .attr("class", "track-inset")
        .select(function() { return this.parentNode.appendChild(this.cloneNode(true)); })
        .attr("class", "track-overlay")
        .call(d3.drag()
            .on("start.interrupt", function() { slider.interrupt(); })
            .on("start drag", function() { hue(sliderx.invert(d3.event.x)); }));

    slider.insert("g", ".track-overlay")
        .attr("class", "ticks")
        .attr("transform", "translate(0," + 18 + ")")
        .selectAll("text")
        .data(sliderx.ticks(10)) //10 slots, 10 dates, therefore, generate_date should be modified when using real dataset!!!
        .enter().append("text")
        .attr("x", sliderx)
        .attr("text-anchor", "middle")
        .text(function(d) { return generate_date(d); });

    var handle = slider.insert("circle", ".track-overlay").attr("class", "handle").attr("r", 9);

    slider.transition().duration(750).tween("hue", function() {
        var i = d3.interpolate(0, 20);
        return function(t) { hue(i(t)); };
    });

    function get_price_for(county_id, current_index) {
        var all_prices = all_date_data[current_index]["all_prices"];
        for (var i = 0; i < all_prices.length; i++) {
            element = all_prices[i];
            if (parseInt(element.county) == parseInt(county_id)) {
                return element["price"];
            }
        }
        return 233; //if county id doesn't match. 
    }

    function hue(h) {
        handle.attr("cx", sliderx(h));
        current_index = Math.floor(h); //index-related heatmap color
        //console.log("index:" + current_index);

        //[1]redraw date
        date_selected[0] = all_date_data[current_index]["date"];
        redraw_text(date_svg_text, date_selected, function(d) { return d; });
        //[2]update heatmap 
        var hg = d3.select("#usmap_svg").selectAll("g").selectAll("path").data(topojson.feature(county_map_json, county_map_json.objects.counties).features);
        hg.style("fill", function(d) { //to be done,
            var tmp = get_price_for(d.id, current_index);
            return heatmap_color(tmp % 10);
        });
    }


    //-----------------------------------------------
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
        .text("Heat");

    heatmap_legend.call(d3.axisBottom(heatmap_linearscale)
            .tickSize(13)
            .tickFormat(function(x2, i) { return i ? x2 : x2 + "/10"; })
            .tickValues(heatmap_color.domain()))
        .select(".domain")
        .remove();

    var heatmap_g = heatmap_svg.append("g");

    heatmap_g.append("g")
        .attr("id", "counties")
        .selectAll("path")
        .data(topojson.feature(county_map_json, county_map_json.objects.counties).features)
        .enter().append("path")
        .on("click", function(d) {
            show_county_info(d.id);
            zoom_and_move(d);
        })
        //.attr("fill", function(d) { return heatmap_color(d.rate = 3 % 10); }) //TBD
        .attr("d", heatmap_path)
        .append("title")
        .text(function(d) { return "Region ID:" + d.id + ", Rating:" + d.rate + "(/10)"; });

    heatmap_g.append("path")
        .datum(topojson.mesh(county_map_json, county_map_json.objects.states, function(a, b) { return a !== b; }))
        .attr("id", "states")
        .attr("d", heatmap_path);

    //------------------------date svg----------------------------------
    var date_selected = ["---"];
    var date_svg = d3.select("#date_svg");
    var date_svg_text = date_svg.append('text')
        .data(date_selected)
        .attr('x', 100)
        .attr('y', 60)
        .attr('fill', '#000')
        .style("font-size", "44px")
        .classed('date_selected', true)
        .text(function(d) { return d; });

    //------------------------redio buttons-----------------------------
    var radio_svg = d3.select("#radio_svg")
        .attr("width", 700)
        .attr("height", 300);

    var number = radio_svg.append("text")
        .attr("id", "numberToggle")
        .attr("x", 120)
        .attr("y", 90)
        .attr("fill", "green")
        .attr("font-size", 24)
        .text("[Choose a metric]")

    var allButtons = radio_svg.append("g")
        .attr("id", "allButtons")

    //fontawesome button labels
    var labels = ['Metric1', 'Metric2', 'Metric3'];

    //colors for different button states 
    var defaultColor = "#7777BB"
    var hoverColor = "#0000ff"
    var pressedColor = "#000077"

    //groups for each button (which will hold a rect and text)
    var buttonGroups = allButtons.selectAll("g.button")
        .data(labels)
        .enter()
        .append("g")
        .attr("class", "button")
        .style("cursor", "pointer")
        .on("click", function(d, i) {
            updateButtonColors(d3.select(this), d3.select(this.parentNode));
            d3.select("#numberToggle").text(labels[i] + " is selected.");
            //TODO: redraw_heatmap

        })
        .on("mouseover", function() {
            if (d3.select(this).select("rect").attr("fill") != pressedColor) {
                d3.select(this).select("rect").attr("fill", hoverColor);
            }
        })
        .on("mouseout", function() {
            if (d3.select(this).select("rect").attr("fill") != pressedColor) {
                d3.select(this).select("rect").attr("fill", defaultColor);
            }
        })

    var bWidth = 140; //button width
    var bHeight = 55; //button height
    var bSpace = 20; //space between buttons
    var x0 = 20; //x offset
    var y0 = 10; //y offset

    //adding a rect to each toggle button group
    //rx and ry give the rect rounded corner
    buttonGroups.append("rect")
        .attr("class", "buttonRect")
        .attr("width", bWidth)
        .attr("height", bHeight)
        .attr("x", function(d, i) { return x0 + (bWidth + bSpace) * i; })
        .attr("y", y0)
        .attr("rx", 5) //rx and ry give the buttons rounded corners
        .attr("ry", 5)
        .attr("fill", defaultColor)

    //adding text to each toggle button group, centered 
    //within the toggle button rect
    buttonGroups.append("text")
        .attr("class", "buttonText")
        .attr("font-family", "FontAwesome")
        .attr("x", function(d, i) {
            return x0 + (bWidth + bSpace) * i + bWidth / 2;
        })
        .attr("y", y0 + bHeight / 2)
        .attr("text-anchor", "middle")
        .attr("dominant-baseline", "central")
        .attr("fill", "white")
        .text(function(d) { return d; })


    function updateButtonColors(button, parent) {
        parent.selectAll("rect").attr("fill", defaultColor)
        button.select("rect").attr("fill", pressedColor)
    }

    //zoom in and zoom out 
    function zoom_and_move(d) {
        var x, y, k;
        if (d && heatmap_svg_centered !== d) {
            var centroid = heatmap_path.centroid(d);
            x = centroid[0];
            y = centroid[1];
            k = 4;
            heatmap_svg_centered = d;
        } else {
            x = heatmap_svg_width / 2;
            y = heatmap_svg_height / 2;
            k = 1;
            heatmap_svg_centered = null;
        }
        heatmap_g.selectAll("path").classed("active", heatmap_svg_centered && function(d) { return d === heatmap_svg_centered; });
        heatmap_g.transition()
            .duration(750)
            .attr("transform", "translate(" + heatmap_svg_width / 2 + "," + heatmap_svg_height / 2 + ")scale(" + k + ")translate(" + -x + "," + -y + ")")
            .style("stroke-width", 1.5 / k + "px");
    }

    //update county info on click, call /county/<id> api!
    function show_county_info(county_id) {
        queue().defer(d3.json, "/county/" + county_id).await(county_charts);
    }
    //update county info on click, draw charts and labels!
    function county_charts(error, county_json) {
        var county = county_json["county"]; //county name
        var rate = +county_json["rate"];
        var history = county_json["history"];
        var stocks = county_json["stocks"];
        //parse date
        var dateFormat = d3.time.format("%Y-%m");
        history.forEach(function(t) {
            t["date"] = dateFormat.parse(t["date"]);
            t["date"].setDate(1);
        });
        //region and rating
        region_selected[0].name = county;
        redraw_text(region_svg_text, region_selected, function(d) { return d.name; });
        rating_selected[0] = rate;
        redraw_text(rating_svg_text, rating_selected, function(d) { return d; });
        //time chart
        var data = [];
        show_prediction_chart(history, data);
    }

    function show_prediction_chart(history, data) {
        var selectorOptions = {
            buttons: [{
                step: 'month',
                stepmode: 'backward',
                count: 1,
                label: '1m'
            }, {
                step: 'month',
                stepmode: 'backward',
                count: 6,
                label: '6m'
            }, {
                step: 'year',
                stepmode: 'todate',
                count: 1,
                label: 'YTD'
            }, {
                step: 'year',
                stepmode: 'backward',
                count: 1,
                label: '1y'
            }, {
                step: 'all',
            }],
        };
        var layout = {
            title: 'Historical Real Estate Price',
            xaxis: {
                rangeselector: selectorOptions,
                rangeslider: {}
            },
            yaxis: {
                fixedrange: true
            }
        };

        data = [];
        data.push(trace0_price(history));
        for (i = 0; i < 5; i++) {
            data.push(trace1_s1(history, i));
        }
        Plotly.newPlot('prediction_chart_div', data, layout);

        function trace0_price(history) {
            var x = [];
            var y = [];
            history.forEach(function(datum) {
                x.push(datum["date"]);
                y.push(datum["price"]);
            });
            return { x: x, y: y, mode: 'lines', type: 'scatter', name: 'price' };
        }

        function trace1_s1(history, index_) {
            var x = [];
            var y = [];
            history.forEach(function(datum) {
                x.push(datum["date"]);
                y.push(datum["stocks"][index_]);
            });
            return { x: x, y: y, mode: 'lines', type: 'scatter', name: ("stock" + index_) };
        }


    }
}