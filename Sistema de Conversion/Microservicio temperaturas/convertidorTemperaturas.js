function convertirTemperatura(temperatura, conversionType) {
    let result;

    switch (conversionType) {
        case "celsiusToFahrenheit":
            result = (temperatura * 9/5) + 32;
            break;
        case "fahrenheitToCelsius":
            result = (temperatura - 32) * 5/9;
            break;
            case "celsiusToKelvin":
                result = temperatura + 273.15;
                break;
            case "kelvinToCelsius":
                result = temperatura - 273.15;
                break;
        default:
            result = "Conversión no válida";
    }

    return result.toFixed(2);
}

module.exports = convertirTemperatura;