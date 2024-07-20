var token = "";
var type = "ADDRESS";
var $city = $("#id_city");

var defaultFormatResult = $.Suggestions.prototype.formatResult;

function formatResult(value, currentValue, suggestion, options) {
    var newValue = suggestion.data.city;
    suggestion.value = newValue;
    return defaultFormatResult.call(this, newValue, currentValue, suggestion, options);
}

function formatSelected(suggestion) {
    return suggestion.data.city;
}

// город и населенный пункт
$city.suggestions({
    token: token,
    type: type,
    // hint: false,
    bounds: "city",
    constraints: {
        locations: { city_type_full: "город" }
    },
    formatResult: formatResult,
    formatSelected: formatSelected,
    onSelect: function (suggestion) {
        console.log(suggestion);
    }
});
