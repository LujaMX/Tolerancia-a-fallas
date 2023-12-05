// calcular.js
function calcular(num1, operator, num2) {
    var result;

    switch (operator) {
        case "+":
            result = num1 + num2;
            break;
        case "-":
            result = num1 - num2;
            break;
        case "*":
            result = num1 * num2;
            break;
        case "/":
            if (num2 !== 0) {
                result = num1 / num2;
            } else {
                return "No se puede dividir por cero";
            }
            break;
        default:
            return "Seleccione un operador válido";
    }

    return "Resultado: " + result.toFixed(2);
}

// Exporta la función para que pueda ser utilizada en otros archivos
module.exports = calcular;
