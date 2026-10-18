# Memória do projeto — Ferreira Motores

Este documento registra as decisões aprovadas e os resultados
históricos desta conversa. Antes de novas alterações, conferir
o código atual. Não considerar testes antigos como validação
automática de uma nova versão.

## Preferência permanente de avaliação

- O usuário quer receber avaliações com notas de 0 a 100 por categoria, conforme o que cada skill consegue medir ou avaliar por critérios documentados.
- Mostrar origem, método, cenário (por exemplo, celular/computador), cobertura e limitações. Usar notas reais de ferramentas ou identificar explicitamente um índice de checklist calculado.
- Não inventar notas nem tratar itens não executados como aprovados. Usar “não avaliado” quando não houver evidência e indicar notas parciais quando houver verificações pendentes.
- Em comparações antes/depois, manter o mesmo cenário e os mesmos critérios; não reutilizar notas antigas como medições atuais.
- Regra registrada também no AGENTS.md e no guia portátil da skill melhorar-html: .agents/skills/melhorar-html/references/avaliacoes.md. A regra se aplica aos relatórios enviados ao usuário, sem adicionar notas à página pública do site.

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

## ZIP pronto para Hostinger

- Atualizado Ferreira-Motores-Site-v2.zip com o index.html atual e todos os arquivos de assets/, sem pasta intermediária.
- Pacote com 32 arquivos; arquivos do ZIP com permissões 0644. Não inclui Git, instruções internas ou HTML independente duplicado.
- Horários apenas na tabela amarela ao final de Fale conosco e Instagram mantido.
- Verificados integridade ZIP, igualdade com os fontes e HTTP 200 da página e de 19 recursos locais, incluindo fundos CSS.
- Conteúdo extraído validado em Chromium/Playwright em 375, 768 e 1440 pixels: tabela única amarela ao final, imagens, âncoras, menu e FAQ.
- Para instalar: enviar o ZIP ao public_html do domínio na Hostinger e extrair ali; index.html e assets/ devem ficar diretamente nessa pasta. Salvar uma cópia dos arquivos anteriores antes de substituí-los. Não exige npm ou build.
- Upload e validação no domínio da Hostinger ainda não realizados.

## Instalação das skills de SEO na readme-edits

- Extraídas seo-audit e seo-audit-full do ZIP enviado para .agents/skills/, preservando scripts, referências e modelos; incluída licença MIT em cada pasta.
- Guia em português em .agents/skills/README.md e dependências reproduzíveis em requirements-seo-audit.txt. Ambiente Python preparado fora do checkout em /workspace/seo-audit-tools/venv.
- Verificados os dez comandos --help, análise JSON-LD local (pass nas duas skills), metadados sociais (warn do conteúdo) e pip check. Não executada auditoria completa nem descoberta automática em nova sessão.
- Site e ZIP da Hostinger preservados; instalação apenas na branch readme-edits para revisão e posterior merge. A auditoria completa precisará de chave PageSpeed, não necessária à instalação.

## Correção da galeria e metadados na readme-edits

- Domínio oficial informado pelo usuário: https://www.ferreiramotores.com.br/.
- Adicionados canonical e og:url; imagens Open Graph/Twitter alinhadas ao mesmo domínio nas duas versões HTML.
- Galeria com tabindex=0, região nomeada e contorno azul de foco visível; navegação nativa com setas mantida no celular.
- Atualizado o ZIP para Hostinger, preservando index.html na raiz e os 31 arquivos de assets/. As skills e os relatórios não fazem parte do ZIP.
- Validação local das três versões (HTML, independente e ZIP extraído) em 375, 768 e 1440 pixels: galeria alcançada com Tab, foco visível, setas no celular, ausência de violações no axe-core executado, metadados corretos, menu, Escape, FAQ, imagens, âncoras e horários únicos ao final.
- Validadores originais: canonical, JSON-LD e metadados sociais passaram nos dois HTMLs. Permanecem limitações de contraste que exigem revisão manual; não declarada conformidade WCAG completa.
- Não validados domínio público, redirecionamentos ou hospedagem. Alterações destinadas somente à branch readme-edits, sem merge na main.

## Skill reutilizável melhorar-html

- Criada a skill original .agents/skills/melhorar-html/SKILL.md, com checklist e exemplos para este projeto e novos sites.
- Orienta melhorias de layout, responsividade, acessibilidade, SEO e desempenho, com preservação de identidade, dados comerciais, branches e autorização de publicação. Instruções específicas continuam nos AGENTS.md e skills do projeto.
- Não exige dependências por si só e não inclui domínio, empresa ou caminhos de ambiente fixos. O guia explica como copiar a pasta completa para outros repositórios.
- Publii-master.zip e ant-design-landing-master.zip inspecionados: não contêm SKILL.md. Pacotes preservados; não incorporados ao site nem à skill.
- Validadas estrutura, frontmatter, referências locais e cópia portátil em ZIP separado. Descoberta em uma nova sessão e execução em outro projeto não foram verificadas.
- Alterações somente de skill/documentação na readme-edits; HTML, imagens e ZIP de hospedagem preservados.

## Otimizações de imagens e contraste na readme-edits

- Mantidos os originais e criadas 30 variantes WebP responsivas com Sharp 0.35.5. HTML principal com srcset/sizes; imagem principal prioritária.
- Cartões de serviço com gradiente de proteção do texto; apresentação entre 621 e 1100 pixels separa texto, motor e faixa amarela. Parágrafo limitado no computador para evitar sobreposição.
- Geradores reproduzíveis para variantes, HTML independente e ZIP publicável em scripts/. Instruções e resultados documentados no README.md geral.
- HTML independente reduzido em 38%: 1.706.546 → 1.057.241 bytes. ZIP contém 48 arquivos referenciados, sem ferramentas, skills ou relatórios.
- Lighthouse local, execuções novas: desempenho principal 99/100 celular e 100/100 computador; independente 63/100 celular (antes 57) e 96/100 computador (antes 88). Acessibilidade automática, boas práticas e SEO 100/100 nos quatro cenários.
- Dados transferidos no principal: redução de 26% no celular e 50% no computador. Medições de laboratório, sem validação da hospedagem ou do file://.
- Checklist funcional 100/100 calculado, 18/18 critérios, 130 verificações nos dois HTMLs; axe-core sem violações automáticas, com contraste complexo ainda marcado como inconclusivo pela ferramenta. Revisão por amostragem e cálculo conservador dos fundos aplicada, sem declaração de conformidade WCAG completa.
- Pacote extraído conferido; contatos, identidade visual, dados comerciais e horários somente na tabela amarela ao final preservados. Alterações destinadas à readme-edits, sem merge na main.

## Restauração das imagens e do contraste anteriores

- O usuário esclareceu que preferia as imagens e o contraste da versão anterior, sem desfazer as demais melhorias.
- Restaurados os 14 elementos de imagem, os dois fundos de serviços e o gradiente exatos do commit b017f6f. Removida a seleção das variantes recomprimidas no HTML; fotografias e logo originais preservados.
- Mantidos ajustes de layout em tablet/computador, galeria por teclado, metadados, skills, preferência por avaliações fundamentadas e horários somente na tabela amarela final.
- Regenerados HTML independente e ZIP da Hostinger. Mantida a deduplicação dos fundos incorporados; ZIP com index.html na raiz e somente 19 assets referenciados. Integridade e igualdade dos arquivos do pacote com os fontes conferidas.
- Chromium/Playwright: 130 verificações funcionais aprovadas nos dois HTMLs em 320, 375, 768 e 1440 pixels. axe-core sem violações automáticas; contraste complexo continua inconclusivo, sem declaração de conformidade completa.
- README atualizado para distinguir a restauração das medições históricas; Lighthouse não reexecutado nesta alteração.
- Preservar este tratamento visual de imagens e contraste em futuras melhorias. Alteração destinada à readme-edits; sem merge na main ou upload à Hostinger.

## Página 404 personalizada e favicon para a busca

- Criada 404.html com o logo original, identidade amarela/preta, botões para início e contato, foco visível e noindex. Recursos usam caminhos a partir da raiz para funcionar em URLs inexistentes de subpastas.
- Incluído .htaccess com ErrorDocument 404 /404.html, sem redirecionar à home; preservar outras regras existentes na instalação.
- Acrescentados favicon PNG 96 × 96 e ICO com 64/48/32/16 pixels, convertidos do logo existente. O favicon WebP anterior tinha 64 × 64 e já era quadrado: não comprovada a causa de sua ausência no resultado do Google.
- Sincronizados os dois HTMLs e o ZIP; geradores atualizados para incluir a 404, sua configuração e os ícones. Site principal mantém imagens, contraste, horários e demais decisões aprovadas.
- ZIP íntegro com 23 arquivos, todos iguais aos fontes. Testados aparência, logo, links, ícones via HTTP, foco e axe-core da 404 no pacote extraído em 375, 768 e 1440 pixels; sem violações automáticas. Revalidados ambos os HTMLs nas mesmas larguras, com 96 verificações funcionais aprovadas; contraste complexo do site principal segue inconclusivo pela ferramenta.
- README orienta envio ao public_html, preservação do .htaccess anterior, teste de status 404 na hospedagem e solicitação de indexação da página inicial no Search Console. Atualização do favicon no Google depende de rastreamento e seleção do buscador, sem prazo garantido.
- Acesso ao domínio bloqueado pelo proxy deste ambiente, não um erro comprovado do site. Não validados hospedagem, regra .htaccess em Apache/LiteSpeed, acesso de Googlebot-Image ou Search Console. Sem upload à Hostinger ou alteração da main; trabalho salvo na readme-edits.

## Arte de apresentação com motor azul; favicon original mantido

- O usuário informou que as imagens passaram a aparecer no Google e pediu mais identidade na apresentação. Durante a criação, esclareceu: manter o logo completo no favicon e trocar somente o motor da arte pelo azul, sem fundo branco.
- Decisão final: favicon.ico e assets/favicon-96x96.png preservados byte a byte em relação ao commit cde04ad. Opção simplificada FM não aplicada; evitar substituir o logo por monograma sem novo pedido.
- Criada assets/brand/ferreira-motores-apresentacao.jpg, 1200 × 1200, com motor azul sobre bancada e moldura preta/amarela, logo e textos da composição apresentada. Arte gerada com referências do logo, do motor de assets/nova/motor-hero-clean.webp e da bancada de assets/IMG-20261003-WA0009.webp; não apresentar como fotografia documental de um serviço específico.
- Metadados Open Graph/Twitter e image do LocalBusiness apontam para a nova arte. Incluídos max-image-preview:large, URL e logo da empresa no JSON-LD, mantendo dados comerciais. Isso oferece uma imagem representativa e não determina a miniatura escolhida pelo Google.
- Preservados conteúdo visível e CSS do site, fotos originais, logo do cabeçalho, página 404, configuração de erro e horários somente no quadro amarelo final.
- Sincronizados HTML independente e pacote Hostinger; gerador inclui também imagens absolutas dos metadados/JSON-LD. ZIP íntegro com 25 arquivos iguais aos fontes, sem skills, ferramentas ou matriz da opção FM descartada.
- Chromium/Playwright: versões principal, independente e ZIP extraído passaram em 375, 768 e 1440 pixels (nove cenários). Verificados imagens, ícones, arte acessível via HTTP local, metadados/JSON-LD, ausência de transbordamento, menu/Escape, galeria, FAQ, horários finais e erros JavaScript. Página 404 e dimensões das imagens também conferidas.
- axe-core WCAG A/AA na versão móvel principal sem violações automáticas; contraste complexo ainda inconclusivo. Execução geral mostrou recomendação region no botão flutuante, reproduzida sem alterações no baseline anterior; sem nova falha introduzida ou declaração de conformidade completa.
- Sem nova medição Lighthouse, acesso ao domínio ou validação de indexação. Atualização destinada à readme-edits; main e hospedagem não alteradas. Publicação do pacote e novo rastreamento ficam pendentes; o Google pode escolher outra foto mesmo após a atualização.
