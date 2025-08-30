$(document).ready(function () {
    $('#id_city').on('change blur', function () {
        var city = $(this).val();
        if (city.length > 2) {
            var apiKey = "af2a48c09a554a0b206f8fa58a30dc97";
            var url = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}&units=metric`;

            $.getJSON(url, function (data) {
                $('#id_temperature').val(data.main.temp);
                $('#id_humidity').val(data.main.humidity);
            }).fail(function () {
                alert("⚠️ Unable to fetch weather for this city. Please check the name.");
            });
        }
    });
});
