// Call the dataTables jQuery plugin
$(document).ready(function() {
  $('#dataTable').DataTable({
    "ordering": true,               // Allows ordering
    "searching": true,              // Searchbox
    "paging": false,                 // Pagination
    "info": false,                  // Shows 'Showing X of X' information
    "columnDefs": [
        {
            "targets": 'dialPlanButtons',
            "searchable": false,    // Stops search in the fields 
            "sorting": false,       // Stops sorting
            "orderable": false      // Stops ordering
        }
    ],
    "dom": '<"top"f>rt<"bottom"lp><"clear">', // Positions table elements
    "language": {
        "search": "_INPUT_",            // Removes the 'Search' field label
        "searchPlaceholder": "검색"   // Placeholder for the search box
    },
    "search": {
        "addClass": 'form-control input-lg col-xs-12'
    },
    "fnDrawCallback":function(){
        $("input[type='search']").attr("id", "searchBox");
        $('#dialPlanListTable').css('cssText', "margin-top: 0px !important;");
        $("select[name='dialPlanListTable_length'], #searchBox").removeClass("input-sm");
        $('#searchBox').css("width", "300px").focus();
        $('#dialPlanListTable_filter').removeClass('dataTables_filter');
    }
});
});
