 $('.btn').on('click', function () {
        $('.btn').removeClass('selected');
        $(this).addClass('selected');

    })
    $('#battery').on('click', function () {
            
        var progressDiv = $('<div class="progress">');
        var progressBar = $('<div id="prog" class="progress-bar progress-bar-striped progress-bar-animated text-center" role="progressbar" aria-valuemin="0" aria-valuemax="100">');
        $(function () {
            $.getJSON('/chargeLevel',
                function (data) {
                    progressBar.text(data + "%");
                    //do nothing
                    if (data < 35) {
                        progressBar.addClass('bg-danger');
                    } else if (data < 55) {
                        progressBar.addClass('bg-warning');
                    } else {
                        progressBar.addClass('bg-success');
                    }
                    progressBar.width(data + '%').attr('aria-valuenow', data);
                   
                    console.log(data + " : Charge Level")
                    return false;
                });
        });
        $(progressBar).appendTo(progressDiv);
        $(progressDiv).appendTo('.myBar');
    });

    $(function () {
        $.getJSON('/isCharge',
            function (data) {
                if (data == "1") {
                    console.log("CHARGING");
                
                } else {
                    $('#charg').remove();
                    $('#move').text('Not Charging');
                    console.log("NOT CHARGING");
                }
                return false;
            });
    });