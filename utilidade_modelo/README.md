# Agentes Baseados Em Atividade
Um agente baseado na utilidade é um tipo de agente que toma as decisões com base na avaliação de potenciais resultados com base na conveniência dessas decisões. Estes agentes procuram maximizar o seu desempenho global, selecionando ações que conduzam aos resultados mais favoráveis.
 *


Vou criar um exemplo simples de um agente baseado em modelo em Python, onde o agente decide se deve ir para academia ou não sair de casa com base em algumas condições climáticas.

Neste exemplo, temos a classe ModelBasedAgent, que representa nosso agente. Ele recebe a temperatura e o tempo como parâmetros ao ser inicializado. O método decide() é responsável por tomar a decisão com base nessas informações.

Em seguida, temos a função simulate_enviroment(), que usa A API de do climatempo. Veja a documentação completa no site oficial: https://advisor.climatempo.com.br/.

Na função principal main(), obtemos a temperatura e o tempo do ambiente, criamos uma instância do agente e solicitamos que ele tome uma decisão com base nessas informações. Em seguida, imprimimos a decisão do agente.