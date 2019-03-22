$(document).ready(function () {
    alert("loaded!");

    // page initial
    $("#rpt_list tbody tr").each(function () {
        $(this).unbind("click").on("click", function(){
            // alert($(this).attr("rpt_id") + $(this).children().eq(1).text());
            var rpt_id = $(this).attr("rpt_id");
            window.location.href = "/rpt/" + rpt_id;
        });
    });
});