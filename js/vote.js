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




