---
name: melhorar-html
description: "Melhorar páginas e sites existentes em HTML, CSS e JavaScript: layout, responsividade, acessibilidade, SEO e desempenho. Use para pedidos de melhorar, revisar ou corrigir uma página, landing page, site institucional, menu, galeria, formulário ou versão móvel. Respeite a tecnologia e a identidade do projeto; não migre automaticamente para frameworks."
---

# Melhorar HTML

Conduza o trabalho do diagnóstico à implementação e validação. Esta skill é
reutilizável: descubra as regras e os caminhos do projeto atual, sem presumir uma
empresa, idioma, domínio, ferramenta de hospedagem ou estrutura de pastas.

## 1. Definir o escopo e preservar o trabalho existente

- Leia os AGENTS.md aplicáveis, documentação e skills específicas do projeto.
  Preserve as decisões aprovadas e siga as instruções do usuário.
- Confira branch, mudanças locais e arquivos não versionados antes de editar.
  Use o checkout existente. Não crie worktrees sem pedido.
- Descubra páginas de entrada, estilos, scripts, imagens, versões independentes,
  fontes de geração, manifests, comandos e artefatos de publicação.
- Em projetos com templates ou geração, altere a fonte apropriada e use o build
  documentado. Não edite apenas um arquivo gerado que será sobrescrito.
- Diferencie os pedidos: em uma auditoria, apresente achados; em uma implementação,
  aplique o ajuste solicitado. Criar ou instalar esta skill não autoriza redesenhar
  o site. Use escolhas razoáveis e pergunte apenas por informações que bloqueiam
  um resultado correto, como dados comerciais ausentes ou domínio desconhecido.
- Respeite a branch pedida. Não una com a principal por consequência de um commit.

## 2. Fazer um diagnóstico proporcional

- Leia a página e confira o comportamento atual antes de mudar o visual.
- Traduza o pedido em um resultado verificável: por exemplo, um menu que fecha com
  Escape, uma galeria alcançável com Tab ou uma seção legível sem transbordamento.
- Faça uma captura ou registre medidas do estado anterior quando isso ajudar a
  comparar layout. Relacione cada mudança a um problema ou objetivo do pedido.
- Para melhorias amplas, priorize falhas funcionais, clareza da informação,
  navegação por teclado e legibilidade; depois faça refinamentos de aparência.
- Uma auditoria local não estabelece comportamento da hospedagem ou de APIs.

## 3. Implementar com a tecnologia e a identidade existentes

- Mantenha linguagem, marca, cores aprovadas, contatos, endereços, horários e links.
  Não invente preços, avaliações, certificados ou informações comerciais.
- Ajuste hierarquia visual, espaçamento, alinhamento, largura dos textos e tamanho
  dos controles com uma intenção clara. Reaproveite os tokens e estilos existentes.
- Preserve a composição aprovada fora do trecho solicitado; evite reescrever a
  página inteira por um ajuste pontual ou acumular regras CSS contraditórias.
- Para sites simples, prefira HTML semântico, CSS e JavaScript simples. Adicione
  dependências apenas se resolverem uma necessidade concreta do pedido.
- Em projetos que já usam um framework, siga suas convenções; uma biblioteca de
  templates não é uma skill e sua importação não é necessária para esta rotina.
- Preserve a ordem de leitura e o conteúdo em telas pequenas. Corrija a causa de
  transbordamentos, sem esconder o problema com overflow-x:hidden na página toda.
- Galerias podem ter rolagem horizontal intencional. Forneça acesso por teclado,
  identificação acessível e indicação clara de foco; mantenha o gesto de toque.
- Implemente movimentos sem esconder conteúdo de forma permanente. Respeite
  prefers-reduced-motion e preserve acesso às informações essenciais sem animação.

## 4. Acessibilidade, conteúdo e SEO

- Use elementos nativos: links para navegação, botões para ações, labels em campos,
  títulos em hierarquia coerente e tabelas para informações tabulares.
- Confira Tab/Shift+Tab, Enter/Espaço, Escape quando aplicável, foco visível e
  retorno de foco. Sincronize aria-expanded e estados de menus com o que aparece.
- Contêineres que precisam de foco podem usar tabindex="0". Evite tabindex positivo
  e ARIA redundante; regiões devem ter nomes compreensíveis. Verifique contraste
  do indicador de foco contra o fundo real, não apenas sua existência em CSS.
- Mantenha lang e descrições úteis das imagens. Imagens decorativas podem ter
  alt=""; não preencha o alt com repetição artificial de palavras-chave.
- Mantenha título, descrição, conteúdo visível e dados estruturados coerentes.
  Títulos de busca não têm um limite universal rígido de caracteres.
- Confirme o domínio antes de definir canonical, og:url ou URLs sociais absolutas.
  Não use localhost como endereço oficial, nem invente domínio, redirects ou regras
  da hospedagem. Preserve variantes legítimas que tenham canonical próprio.
- Use as skills de SEO disponíveis quando uma análise aprofundada for solicitada.
  Não altere o texto apenas para satisfazer contagens ou correspondências exatas.

## 5. Imagens e desempenho

- Confira arquivos, dimensões e finalidade antes de otimizar. Preserve fotografias
  reais, proporções e qualidade perceptível.
- Quando útil, ofereça versões responsivas com srcset/sizes. Não aplique lazy
  loading à imagem principal se isso prejudicar seu carregamento.
- Evite scripts e fontes desnecessários, duplicação de imagens e mudanças de layout
  por falta de dimensões. Preserve verificação TLS e integridade de dependências.
- Se medir desempenho, registre cenário, ferramenta e limitações. Resultados locais
  são laboratório, não Core Web Vitals reais, ranking ou garantia de produção.

## 6. Validar o resultado

Use o [checklist de validação](references/checklist.md). Execute os comandos e
ferramentas existentes do projeto. Esta skill não exige pacotes por si só; localize
as ferramentas antes de escolher instalações e mantenha ferramentas auxiliares
fora das dependências do site quando isso for apropriado.

- Confira, por padrão, larguras de 375, 768 e 1440 pixels; inclua limites de
  breakpoint ou telas menores quando o pedido ou a página justificarem.
- Use Playwright ou ferramenta equivalente, se disponível, e teste ações reais.
  Uma porta aberta ou uma captura de tela sozinha não demonstra funcionamento.
- Confira imagens, âncoras, navegação, menu móvel, galerias, FAQ e formulários
  relevantes ao ajuste. Não envie mensagens, chamadas ou formulários de clientes
  como efeito colateral de uma validação; use ambiente/fixture de teste adequado.
- Use axe-core quando disponível e examine resultados inconclusivos. Testes
  automáticos não comprovam conformidade WCAG completa.
- Reexecute os testes afetados depois de corrigir falhas. Diferencie problemas do
  código, limitações de ferramentas/rede e verificações não executadas.
- Rode lint, build ou testes existentes quando necessários. Não crie testes
  triviais que apenas reproduzem a implementação de um ajuste cosmético.

## 7. Sincronizar e entregar

- Atualize versões independentes quando isso fizer parte das regras do projeto.
  Para ZIPs, primeiro confirme o escopo já autorizado: não recompacte arquivos
  anteriores sem pedido, nem sobrescreva arquivos desconhecidos.
- Quando o pacote estiver no escopo, monte somente os arquivos publicáveis,
  preserve permissões adequadas, confira integridade e teste o conteúdo extraído.
  Não inclua .git, skills, credenciais ou ferramentas de desenvolvimento no site.
- Confira o diff e preserve alterações que não são suas. Faça commit/push na
  branch indicada quando autorizado; publicação, merge e deploy seguem o escopo
  da autorização existente, não acontecem automaticamente por concluir a edição.
- Entregue uma descrição curta: o que mudou, por quê, testes executados e limites.
  Distinga arquivo local, commit remoto e site publicado. Ao fornecer um download,
  explique quando é preciso abrir o novo arquivo em vez de uma cópia antiga.

Consulte [exemplos de uso e portabilidade](references/exemplos.md).
