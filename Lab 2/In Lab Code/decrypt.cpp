#include <iostream>
#include <string>

int main() {
    std::string code;
    std::cout << "Enter the coded text: ";
    std::getline(std::cin, code);

    int distance;
    std::cout << "Enter the distance value: ";
    std::cin >> distance;
    std::cin.ignore(); 

    std::string plainText = "";

    for (char ch : code) {
        if (std::islower(ch)) {
            int base = 'a';
            int ordValue = static_cast<int>(ch);
            int cipherValue = ordValue - distance;
            if (cipherValue < base) {
                cipherValue = base + (ordValue - base - distance) % 26;
            }
            plainText += static_cast<char>(cipherValue);
        } else if (std::isupper(ch)) {
            int base = 'A';
            int ordValue = static_cast<int>(ch);
            int cipherValue = ordValue - distance;
            if (cipherValue < base) {
                cipherValue = base + (ordValue - base - distance) % 26;
            }
            plainText += static_cast<char>(cipherValue);
        } else {
            plainText += ch;
        }
    }

    std::cout << "Message: " << plainText << std::endl;
    return 0;
}
