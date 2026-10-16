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
