var tasklist = [
  {id:0, prio:6, title:"Water leakage"},
  {id:1, prio:5, title:"Coffee shortage"},
  {id:2, prio:4, title:"Overcrowding"},
  {id:3, prio:3, title:"Gas leak"},
  {id:4, prio:2, title:"Leaky window"},
  {id:5, prio:0, title:"Broken handrail"}
]

var prio256 = ['00','2a','54','7e','a8','d2','fc'];

window.onload = function(){
  var table = $("#tasks");
  $.each( tasklist, function(index, task){
    var row = $(document.createElement("tr"));
    var prio = $(document.createElement("td"));
    prio.text(task.prio);
    prio.css('background-color','#FF'+prio256[6-task.prio]+'00');
    prio.width(50);
    var title_ = $(document.createElement("a"));
    title_.attr("href", "details/"+index);
    title_.text(task.title);
    var title = $(document.createElement("td"));
    title.append(title_); 
    row.append(prio,title);
    row.append('<td><a><img src="img/checkmark.png" /></a></td>');
    table.append(row);
  }) 
  setInterval( function(){
    $.ajax('http://136.243.9.146:8442/aechack/v1/sensors/avarage/week/1234567890').done(function(){
      // TODO: check tmpavarage before twitter
      $.ajax('http://136.243.9.146:8442/aechack/v1/tweets/avaragesentiment?text=cool').done(function(){
         // TODO check avaragesentiment add heating task
      });
    }); 
    $.ajax('http://136.243.9.146:8442/aechack/v1/tweets/avaragesentiment?text=coffee').done(function(){
      // TODO check averagesentiment and humidity sensor in coffee pot and add refill task
    }); 
  }, 1000);

}



