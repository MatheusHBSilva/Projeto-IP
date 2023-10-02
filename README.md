# Projeto-IP
Repositório do projeto final de IP
O jogo "Alice in Cocafeland" foi desenvolvido como parte do projeto da disciplina IF668 - Introdução à Programação. Este jogo de plataforma desafia os jogadores a ajudar Alice a encontrar sua coca café perdida, superando obstáculos e coletando moedas para alcançar seu objetivo final.

<div align="center">
<img src="https://github.com/MatheusHBSilva/Projeto-IP/assets/136330380/41ce83db-4c79-467c-b319-7967be10f51d" width="500px" />
</div>

# Execução 

Para execução do código, é necessário que você possua Python e pygame instalados.

Faça o download do branch main deste repositório e extraia o arquivo .zip.
Abra a pasta projetoIP no seu editor de escolha.
Execute o arquivo main.py.

<div align="center">
<img src="https://github.com/MatheusHBSilva/Projeto-IP/assets/136330380/b83b396c-8907-4568-9c5c-1607117dea78" width="1500px" />
</div>

# Movimentação

A Movimentação do jogador dentro do jogo se deve exclusivamente ao espaço, para pular.
Alguns outros botões foram adicionados, como ESC para fechar o jogo.


# Relatório do projeto
     https://www.canva.com/design/DAFvxieky6E/xopJUoeL12OwQvV5SFgZ2g/edit?utm_content=DAFvxieky6E&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton
Link para um Relatório mais aprofundado do projeto


# Ferramentas


1. Piskel: Esta ferramenta foi empregada na criação de pixel arts, incluindo algumas das artes do jogo e elementos do menu.

2. Gimp: Utilizado para edição de imagens, o Gimp desempenhou um papel importante no processo, especialmente no recorte das pixel arts que foram incorporadas ao jogo.

3. Pygame: Essa biblioteca Python foi a espinha dorsal do projeto, usada em todo o código, especialmente no módulo principal do jogo. Pygame é focado no desenvolvimento de jogos 2D e fornece recursos essenciais para a criação de jogos interativos.

4. Random: A biblioteca Random em Python desempenhou um papel fundamental na geração de elementos aleatórios no jogo, como coletáveis (moedas e vidas) e na aleatorização de eventos, tornando o jogo dinâmico.

5. System: A biblioteca System em Python foi utilizada para gerenciar a inicialização e o encerramento do jogo, garantindo um fluxo adequado e controle sobre o ciclo de vida do jogo.



# Problemas e Desafios

Durante a execução do projeto, enfrentamos diversos desafios, sendo um deles particularmente destacado: o planejamento deficiente. Ficou evidente que o planejamento inicial tinha falhas significativas, tanto na concepção quanto na distribuição das tarefas. Em alguns casos, membros trabalharam na mesma parte do projeto de maneiras distintas, devido ao planejamento inadequado. Além disso, a divisão de tarefas não considerou devidamente os aspectos de longo prazo.

Problemas também surgiram em relação à comunicação entre os membros da equipe. A escolha de aplicativos como Discord e WhatsApp para essa finalidade revelou-se insuficiente, pois as mensagens nesses aplicativos podem ser facilmente perdidas ou não visualizadas pelos membros.

Além disso, nossas dificuldades em relação ao conhecimento da biblioteca Pygame e da programação orientada a objetos impactaram significativamente o projeto. A falta de familiaridade com essas tecnologias afetou tanto o planejamento, pois não sabíamos quanto tempo seria necessário para implementar cada função, quanto a execução do projeto, uma vez que o tempo de aprendizado dessas novas tecnologias atrasou tanto a distribuição de tarefas quanto o desenvolvimento em si. 

Em resumo, o grupo enfrentou desafios significativos ao longo do projeto, mas essas dificuldades se transformaram em oportunidades de aprendizado valiosas. A equipe aprendeu não apenas a trabalhar de forma mais eficaz em conjunto, mas também a adquirir conhecimento essencial sobre as tecnologias necessárias para o desenvolvimento do jogo, além de habilidades como gerenciamento de projetos e resolução de problemas.

# Membros da Equipe e suas funções

Abner Adriel(aasl) - Responsável pela criação das artes, implementação das moedas e elaboração do relatório e slide.
Arlindo Silva() - Responsável pela implementação do personagem, elaboração do relatório e slide.
Juan() - Responsável pela implementação da vida.
Matheus Álefe() - Responsável pela criação das artes, implementação dos inimigos e elaboração do relatório.
Matheus Silva() - Responsável pela implementação do áudio, implementação do menu, implementação do main e correção de bugs.


# Organização do código

 

1. Módulo personagem.py: Este módulo é responsável por definir as características e comportamentos do personagem principal do jogo, incluindo sua movimentação e interação com o ambiente.

2. Módulo menu.py: Este módulo cria a interface inicial do jogo, introduzindo o jogador ao ambiente virtual e exibindo as opções disponíveis.

3. Módulo controladora.py: A controladora gerencia o fluxo do jogo, determinando quando e como o jogador avança de nível, carregando recursos e configurando elementos do jogo.

4. Módulo hearts.py: Este módulo controla a mecânica de coleta de corações, que representam a saúde do jogador, incluindo detecção de colisões e atualização da interface.

5. Módulo moedas.py: Responsável pela coleta de moedas no jogo, incluindo a exibição do progresso do jogador na interface e a definição das condições de vitória.

6. Módulo Hud.py: Gerencia elementos da interface, como a barra de vida e o registro de desempenho na coleta de moedas, refletindo as mudanças no estado do jogador.

7. Módulo terrain.py:  Cria o cenário do jogo, incluindo plataformas e obstáculos, proporcionando o ambiente no qual a jogabilidade ocorre.

8. Módulo canhão.py: Responsável pela criação e comportamento do canhão inimigo, incluindo disparos de balas e detecção de colisões com o jogador.

9. Módulo Assets: Armazena todos os recursos visuais e sonoros usados no jogo, como imagens, sprites e arquivos de áudio.

10. Módulo main.py: O módulo central que coordena todas as operações do jogo, incluindo inicialização, execução, gestão de eventos e encerramento do jogo.

# Conceitos Importantes

    Estruturas Condicionais
 As estruturas condicionais( que foram introduzidas no princípio da disciplina foram fundamentais para criar a lógica,o fluxo e os desafios do jogo.Por exemplo, ao detectar uma colisão entre a personagem do jogador e um obstáculo como os disparos do canhão, um bloco de código é executado para lidar com a colisão, como reduzir os pontos de vida do jogador ou reiniciar o nível. Um mecanismo análogo ao funcionamento das colisões com os demais coletaveis.

Além disso, essas estruturas também foram cruciais para a construção da física jogo, bem como para a implementação da lógica de deslocamento da persoangem.As estruturas condicionais podem ser usadas para aplicar efeitos de gravidade à personagem e permitir que ela pule. Por exemplo, a gravidade é aplicada constantemente, mas a personagem só pode saltar quando estiver no chão. Em última instância, as estruturas condicionais foram úteis para definir limites de movimento da personagem, garantindo que ela não saia dos limites do cenário do jogo.

     Laços de repetição
   Os laços foram mais um recurso utiliza do para a concretização do projeto de software interativo. Os loops foram  aproveitados sobretudo para simplificar tarefas repetitivas, como  na implementação de animações e na definição das coordenadas dos elementos coletavies. Ao usar loops "while" e "for", pudemos criar estuturas mais sintéticas e econômicos para determinar se o jogador atingiu os objetivos do jogo.

    Lista
  As listas foram mais um conceito aprendido e que teve participação marcante em  diversas esferas do código-fonte.Esse recurso foi empregado, por exemplo, para  armazenar as coordenadas que delimitam as regiões de posicionamento dos coletaveis, indicando onde esses objetos poderiam aparecer.Essa abordagem reflete as boas práticas de programação ao reduzir a redundância de código e tornar o desenvolvimento e a manutenção do jogo mais eficazes.
  
     Tupla
   As tuplas, embora menos evidentes do que outras estruturas de dados como listas ou classes, desempenharam um papel essencial na nossa implementação. Elas foram empregadas de forma seletiva para atender a requisitos específicos e oferecer vantagens importantes em certos contextos do código.Uma das características marcantes das tuplas é a imutabilidade, o que significa que uma vez criada, uma tupla não pode ser modificada. Isso as tornou ideais para representar coordenadas fixas no nosso jogo, como as posições iniciais de plataformas, objetos colecionáveis e inimigos. Essas coordenadas não deveriam ser alteradas durante a execução do jogo, e as tuplas garantiram que essas posições permanecessem constantes.
