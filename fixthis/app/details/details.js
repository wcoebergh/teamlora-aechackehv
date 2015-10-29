var prio256 = ['00','2a','54','7e','a8','d2','fc'];

window.onload = function(){
  $.each(details, function(k,v){
     $('#'+k).text(v);
  });
  $('#prio').css('background-color','#FF'+prio256[6-details.prio]+'00');
};
