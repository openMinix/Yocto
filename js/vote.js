$(document).ready( setInterval( function (){
       
      var current_posts = $("#conversations").html();
      var latest_post = $($("#conversations").children("article")[0]).attr("id");
      $.ajax({
          url: "/update",
          type: "GET",
          data: { latest_post : latest_post },
          dataType: "text",
          success: function(result){
            $("#conversations").html( result + current_posts );
          }      
     }); 
}, 10000));


$(document).ready( function (){
   $(".btn-vote_up").click( function() {
      
      var post_id = $(this).parent().parent().attr("id");
      var v = $(this).parent().children("strong")[0];
      var current_votes = v.innerHTML;

      $.ajax({
          url: "/vote",
          type: "GET",
          data: {votes: current_votes, sign: "plus", post_id: post_id},
          dataType: "text",
          success: function(result){
            $(v).html(result); 
          }      
     }); 
   });
});


$(document).ready( function (){
   $(".btn-vote_down").click( function() {
      
      var post_id = $(this).parent().parent().attr("id");
      var v = $(this).parent().children("strong")[0];
      var current_votes = v.innerHTML;
      $.ajax({
          url: "/vote",
          type: "GET",
          data: {votes: current_votes, sign: "minus", post_id: post_id},
          dataType: "text",
          success: function(result){
            contents = result.split(" ")
            $(v).html(contents[0]); 
            
          }      
     }); 
   });
});




