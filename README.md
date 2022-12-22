# UFPA Pattern Matching

**University**: Universidade Federal do Pará

**Institute**: Instituto de Ciências Exatas e Naturais

**Faculty**: Faculdade de Computação

**Discipline**: Data Structures II

**Teacher**: FILHO, Reginaldo Cordeiro dos Santos.

**Students**: CARDOSO, Gabriel Santos; SOUZA, Leandro Marcos Pinheiro.

## About the project

This work is a project carried out for the purposes of the Data Structures 2 discipline, taught by Professor Dr. Reginaldo Cordeiro dos Santos Filho, for the Information Systems and Computer Science course at the Faculty of Computing (Faculdade de Computação) – FACOMP, Institute of Exact and Natural Sciences (Instituto de Ciências Exatas e Naturais) – ICEN at the Federal University of Pará (Universidade Federal do Pará) – UFPA.

The project deals with the implementation of brute force algorithms, BMH, BMHS, exact Shift-And and approximate Shift-And (k = 1 and k = 2) in the Python programming language.

## Running code

### Running with SDK

1. To run the project with the SDK you must have the most recent version of Python language installed in your machine.
2. Clone the repository and navigate into then. After that, run the following command to install the requirements
```bash
pip install -r requirements.txt
```
> You must have the latest version of PIP installed in your system. More information [here](https://pip.pypa.io/en/stable/installation/).
3. After it you have to run the following command to run the algorithm with the setted words collection in your `app.ini`
```bash
python3 main.py
```
> This command will run the entrypoint of the program. You could change the words file in your `src/app.ini` in the `[words]` section, `words_file` variable. The words files contains, respectively, `{ (T = 500), (T = 1000), (T = 1500), (T = 2000), (T = 5000) }` where T equals the number of words.

> Also, in this project it's recommended to create a virtual machine to run and test the code. More information about the virtual machine [here](https://www.virtualbox.org/).

### Running with Docker

> Under development

## Licence

This project is licenced under the MIT licence. See [HERE.](LICENSE.md)

## Authors

* [CARDOSO, Gabriel Santos](https://eng-gabrielscardoso.github.io/)
* SOUZA, Leandro Marcos Pinheiro
