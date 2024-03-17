# Agentes Baseados Em Atividade
Um agente baseado na utilidade é um tipo de agente que toma as decisões com base na avaliação de potenciais resultados com base na conveniência dessas decisões. Estes agentes procuram maximizar o seu desempenho global, selecionando ações que conduzam aos resultados mais favoráveis.

- Para demonstração, iremos desenvolver um agente baseado na utilidade em python que deverá decidir entre as seguintes decições: Estudar, Assistir TV, Sair com amigos ou Dormir.
- Note que para cada atividade, temos o seu grau de conveniênvia: Estudar (10), Assistir TV (5), Sair com amigos (8) ou Dormir (12).

Neste exemplo, temos a classe Agente, que representa nosso agente. Ela recebe no seu construtor o parâmetro <strong>self - referênciando a prórpia classe </strong> e <strong> atividade - referênciando ao nosso dicinário de atividades</strong>.

Em seguida, temos o metodo <strong>getAtividade()</strong> - responsável por pecorrer todo o dicionário e retornar a atividade com maior grau de conveniência.

## Testes práticos
Vamos realizar a execução do nosso código
 * <strong> iniciar_agente() - </strong> Função responsável por inicar o nosso agente, definindo e carregando as nossas atividades possíveis em nosso dicionário de dados. Em seguida, temos a criação da instancia do nosso agente, passando por parametro o nosso dicionário de atividades e exibindo no console o resultado escolhido pelo agente.
 