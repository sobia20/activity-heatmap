<template>
  <div id="hasheatmap">
    <meta charset="utf-8" http-equiv="encoding">

    <v-btn color="success" dark large v-on:click="heatmap('http://localhost:5000/activities/activity_count', 'activity_count')">Number of Activity data points</v-btn>
   
    <v-btn color="success" dark large v-on:click="heatmap('http://localhost:5000/activities/max_pchembl_value', 'max_pchembl_value')">Maximum pChEMBL_value</v-btn>
  
    <v-btn color="success" dark large v-on:click="heatmap('http://localhost:5000/activities/avg_pchembl_value', 'avg_pchembl_value')">Average pChEMBL_value</v-btn>
 
    <div id="my_heatmap" ></div>
  </div>
  
</template>

<script src="d3/d3.js" charset="utf-8"></script>
<script charset="utf-8"> 
import * as d3 from 'd3';

var margin = {top: 30, right: 30, bottom: 30, left: 100},
  width = 450 - margin.left - margin.right + 400,
  height = 450 - margin.top - margin.bottom ;

export default {
  name: 'HeatMap',
  methods:{
    heatmap(url_val, color_column){
      d3.select("svg").remove();

      //remove tooltip div if exists
      if (document.getElementById("tools")){
        var div = document.getElementById("tools");
        div.parentNode.removeChild(div);
        }
    // append the svg object to the body of the page
    var svg = d3.select("#my_heatmap")
    .html("<h2> "+color_column)
    .append("svg")
      .attr("width", width + margin.left + margin.right)
      .attr("height", height + margin.top + margin.bottom)
    .append("g")
      .attr("transform",
            "translate(" + margin.left + "," + margin.top + ")");
    
    // Labels of row and columns
    var target_values = ["CHEMBL325",
    "CHEMBL1937",
    "CHEMBL1829",
    "CHEMBL3524",
    "CHEMBL2563",
    "CHEMBL1865",
    "CHEMBL2716",
    "CHEMBL3192",
    "CHEMBL4145",
    "CHEMBL5103",
    "CHEMBL3310"]
    var molecule_values = ["CHEMBL98",
    "CHEMBL99",
    "CHEMBL27759",
    "CHEMBL2018302",
    "CHEMBL483254",
    "CHEMBL1213490",
    "CHEMBL356769",
    "CHEMBL272980",
    "CHEMBL430060",
    "CHEMBL1173445",
    "CHEMBL356066",
    "CHEMBL1914702"]
 
    // Build X scales and axis:
    var x = d3.scaleBand()
      .range([ 0, width ])
      .domain(target_values)
      .padding(0.01);

    svg.append("g")
      .attr("transform", "translate(0," + height + ")")
      .call(d3.axisBottom(x))

    // Build Y scales and axis:
    var y = d3.scaleBand()
      .range([ height, 0 ])
      .domain(molecule_values)
      .padding(0.01);
    
    svg.append("g")
      .call(d3.axisLeft(y));

    d3.json(url_val).then(function(data){

        // Build color scale
        const min = d3.min(data.map(d => d[color_column]));
        const max = d3.max(data.map(d => d[color_column]));
        
        var myColor = d3.scaleLinear()
          .domain([min , max ])
          .range(["#ddeeea", "#69b3a2"]); 
         
        
        // console.log(data);     
        var tooltip = d3.select("#my_heatmap")
          .append("div")
          .style("opacity", 0)
          .attr("id", "tools")
          .attr("class", "tooltip")
          .style("background-color", "#69b3a2")
          .style("border", "solid")
          .style("border-width", "2px")
          .style("border-radius", "5px")
          .style("padding", "5px")
        // Three function that change the tooltip when user hover / move / leave a cell
        var mouseover = function(d) {
          tooltip.style("opacity", 1)
        }
        var mousemove = function(d) {
          tooltip
            .html("The exact value of<br>this cell is: " + d[color_column])
            .style("left", (d3.mouse(this)[0]+70) + "px")
            .style("top", (d3.mouse(this)[1]) + "px")
        }
        var mouseleave = function(d) {
          tooltip.style("opacity", 0)
        }

    // add the squares
    svg.selectAll()
      .data(data, function(d) {
        return d['target']+':'+d['molecule'];})
      .enter()
      .append("rect")
        .attr("x", function(d) { return x(d['target']) })
        .attr("y", function(d) { return y(d['molecule']) })
        .attr("width", x.bandwidth() )
        .attr("height", y.bandwidth() )
        .style("fill", function(d) { return myColor(d[color_column])} )
      .on("mouseover", mouseover)
      .on("mousemove", mousemove)
      .on("mouseleave", mouseleave)

  }) 
    }
  }

}
</script>
<style>
#hasheatmap {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
