# Memória do projeto — Ferreira Motores

Este documento registra as decisões aprovadas e os resultados
históricos desta conversa. Antes de novas alterações, conferir
o código atual. Não considerar testes antigos como validação
automática de uma nova versão.

## Projeto

- Site institucional em português brasileiro.
- Empresa: Ferreira Motores, em Santa Luzia/MG.
- Estrutura simples: HTML, CSS e JavaScript.
- Arquivo principal: index.html.
- Imagens: assets/ e assets/nova/.
- Versão independente, com imagens incorporadas:
  ferreira-motores-completo.html.

## Identidade aprovada

- Preservar amarelo, preto, branco, logo e imagens originais.
- Manter contatos, endereço, horários e links de WhatsApp.
- Não inventar preços, avaliações, garantias ou certificações.
- Imagens dos produtos com fundo e moldura no mesmo branco.
- Faixa amarela para os quatro destaques:
  Desde 2016, Atendimento direto, Orçamento transparente
  e Atuação regional.

## HERO no celular — até 620px

Ordem aprovada:

1. “Seu motor parou? A Ferreira resolve.”
2. Motor inteiro, centralizado, sem cortar a imagem.
3. Linha decorativa amarela abaixo do motor.
4. Texto sobre rebobinagem e manutenção.
5. Benefícios: avaliação técnica, produtos novos e revisados,
   retirada e entrega.
6. Botão “Quero falar com a equipe →”.

Regras:
- Não mostrar “Motores elétricos em Santa Luzia” acima do título.
- Não colocar faixa amarela atrás do motor no celular.
- A linha abaixo do motor tem margens laterais.
- Manter a composição compacta e próxima do cabeçalho.
- Preservar legibilidade e evitar sobreposições.
- A composição foi verificada anteriormente em cinco tamanhos,
  de 320×568 a 430×932, com o CTA na primeira tela.

## HERO no computador

- Preservar a composição aprovada com faixa amarela atrás do motor.
- Benefícios abaixo dos botões, sem sobreposição.
- Alterações destinadas ao celular não devem mudar desktop/tablet.

## Animações

- Entradas ao rolar nas seções e cartões.
- Cada bloco anima uma vez.
- Evitar animações simultâneas no contêiner e nos seus filhos.
- Evitar conflito com efeitos de hover.
- Respeitar prefers-reduced-motion.
- Conteúdo deve continuar acessível sem JavaScript.
- O topo móvel deve ficar imediatamente legível.

## Validações históricas

Ferramentas utilizadas: Playwright, axe-core e Lighthouse.

Verificações realizadas ao longo do desenvolvimento:
- Layout em celular, tablet e computador.
- Menu, Escape, aria-expanded e foco por teclado.
- Atalho “Pular para o conteúdo”.
- Imagens, links internos e perguntas frequentes.
- Destinos de WhatsApp e telefone, sem enviar mensagens.
- Ordem e posicionamento dos elementos da HERO.
- Animações, movimento reduzido e funcionamento sem JavaScript.
- HTML independente com imagens incorporadas.

Resultados anteriores:
- axe-core: zero violações nas verificações executadas.
- Lighthouse local, em revisão anterior:
  desempenho 99; acessibilidade, boas práticas e SEO 100.

Esses resultados não garantem conformidade WCAG completa,
posicionamento no Google nem aprovação de versões posteriores.

## Skills do projeto

- .agents/skills/ferreira-frontend/SKILL.md
- .agents/skills/ferreira-acessibilidade-seo/SKILL.md

## Antes de concluir uma alteração

- Ler AGENTS.md e a skill aplicável.
- Respeitar o escopo solicitado.
- Testar a versão atual, sem reutilizar resultados antigos.
- Atualizar também o HTML independente quando o site mudar.
- Registrar aqui novas decisões e validações, com suas limitações.
- Não publicar ou enviar alterações sem autorização.

## Pendências

- Confirmar a publicação e testar o endereço público.
- Fazer revisão manual de acessibilidade.
- Considerar otimização adicional do tamanho das imagens.

## Instagram

- Adicionado o perfil informado pelo usuário: @ferreiramotoresmg.
- Link na seção de contato das duas versões HTML, abrindo em nova aba.
- Verificados destino, atributos de segurança e consistência entre as versões.
- Renderização e interações no navegador não verificadas nesta alteração.

## Destaque dos horários

- Horários da seção de contato em quadro amarelo, com título e linhas separadas por dia.
- Preservados: segunda a sexta, 8h às 17h; sábado, 9h às 16h; domingo, fechado; aviso sobre urgências.
- Atualizadas as duas versões HTML.
- Verificadas em Chromium com Playwright nas larguras 375, 768 e 1440: quadro sem transbordamento, imagens, âncoras, menu móvel (abertura, Escape e navegação), FAQ e ausência de erros JavaScript.
- Destinos de contato conferidos no HTML; serviços externos não acessados nos testes.

## Horários visíveis no início da página

- Incluído resumo dos horários logo após a apresentação e a faixa de destaques, nas duas versões HTML.
- No computador: três cartões lado a lado; no celular: linhas empilhadas. Adicionado link Horários ao menu.
- Horários comerciais mantidos. Quadro de horários na seção de contato preservado.
- Chromium/Playwright: posição, visibilidade, navegação e ausência de transbordamento do resumo e do menu em 375, 768, 901, 1024 e 1440 pixels, nos dois arquivos.
- Revalidados imagens, âncoras, FAQ, menu móvel e ausência de erros JavaScript em 375, 768 e 1440 pixels, nos dois arquivos.

## Horários somente em Fale conosco

- A pedido do usuário, removidos o resumo de horários do início da página, seu CSS e o atalho Horários do menu.
- Mantido o quadro amarelo com os horários atuais apenas na seção Fale conosco, nas duas versões HTML. Esta decisão substitui a inclusão do resumo superior.
- Chromium/Playwright em 375, 768 e 1440 pixels, nos dois arquivos: um único título de horários em contato, ausência de resumo superior, quadro sem transbordamento, imagens, âncoras, menu móvel e FAQ funcionando, sem erros JavaScript.

## Tabela amarela como último bloco

- Horários aparecem uma única vez, em tabela com fundo amarelo como último bloco de Fale conosco, depois do mapa e de todos os contatos, imediatamente antes do rodapé.
- Tabela ocupa a largura da seção no computador e se adapta ao celular. Nenhum resumo ou atalho de horários no início.
- Duas versões HTML atualizadas; horários comerciais preservados.
- Chromium/Playwright em 375, 768 e 1440 pixels nos dois arquivos: verificados unicidade, posição final, fundo amarelo, três linhas, largura, âncoras, imagens, menu móvel e FAQ; sem erros JavaScript.
