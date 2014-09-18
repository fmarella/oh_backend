$(document).ready(function() {
    $( "#add_dialog" ).dialog({ autoOpen: false, minWidth: 450, minHeight: 200 });

    $( "#add-opener" ).click(function() {
      $( "#add_dialog" ).dialog( "open" );
    });

});
