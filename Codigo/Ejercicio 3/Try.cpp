#include <iostream>
#include <stdexcept> // Necesario para std::invalid_argument

int main() {
    try {
        std::string cadena;
        std::cin >> cadena;
        int numero = std::stoi(cadena); // Intenta convertir la cadena en un entero

        // Si la conversión tiene éxito, imprime el número
        std::cout << "Número convertido: " << numero << std::endl;
    } catch (const std::invalid_argument& e) {
        // Captura una excepción si la conversión falla debido a un argumento no válido
        std::cerr << "Error de conversión: " << e.what() << std::endl;
    } catch (const std::out_of_range& e) {
        // Captura una excepción si la conversión falla debido a un desbordamiento de rango
        std::cerr << "Error de rango: " << e.what() << std::endl;
    }

    return 0;
}
