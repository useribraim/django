(function () {
    var $Select = $("#Select");
    $Select.on("submit", function (e, d) {
        e.preventDefault();
    });
    $Select.on("change", function(e, d) {
        var id = e.target.value;
        location.href = id;

        // ("#Select option[value=id]").attr("selected","selected");
    });
})();