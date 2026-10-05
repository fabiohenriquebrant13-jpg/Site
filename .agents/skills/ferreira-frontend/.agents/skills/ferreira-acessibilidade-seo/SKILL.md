---
name: ferreira-acessibilidade-seo
description: Auditar e melhorar acessibilidade, SEO e desempenho do site Ferreira Motores usando Playwright, axe-core e Lighthouse quando disponíveis.
---

# Acessibilidade e SEO da Ferreira Motores

## Quando usar
Use para auditorias e melhorias de acessibilidade, SEO e desempenho.

## Preparação
- Leia as instruções AGENTS.md aplicáveis.
- Use o checkout existente; não crie worktrees sem pedido.
- Identifique os arquivos do site e as ferramentas disponíveis.
- Preserve alterações existentes e informações comerciais.

## Acessibilidade
- Mantenha lang="pt-BR".
- Confira hierarquia de títulos e estrutura semântica.
- Verifique navegação por teclado e foco visível.
- Confira nomes acessíveis dos botões e links.
- Teste aria-expanded, fechamento do menu e tecla Escape.
- Confira contraste e textos alternativos das imagens.
- Mantenha um título descritivo no iframe do mapa.
- Use axe-core para verificações automatizadas.
- Não declare conformidade WCAG apenas com testes automatizados.

## SEO
- Mantenha título e meta description descritivos.
- Preserve conteúdo coerente com Santa Luzia/MG e região.
- Confira informações de compartilhamento nas redes sociais.
- Confirme a URL pública antes de adicionar canonical
  ou alterar URLs de compartilhamento.
- Não invente avaliações, certificações ou dados comerciais.
- Adicione dados estruturados apenas com informações verificadas.

## Desempenho
- Verifique tamanho, formato e dimensões das imagens.
- Use carregamento tardio nas imagens secundárias quando adequado.
- Evite carregamento tardio da imagem principal se prejudicar o LCP.
- Evite dependências desnecessárias.

## Ferramentas e validação
- Use Playwright para testar comportamento e diferentes telas.
- Use axe-core para identificar problemas de acessibilidade.
- Use Lighthouse para desempenho, acessibilidade,
  boas práticas e SEO.
- Neste ambiente, as ferramentas ficam em
  /workspace/site-dev-tools.
- O teste node smoke.cjs gera axe-report.json.
- Fora deste ambiente, localize ou instale as ferramentas
  antes de executar; estes arquivos não instalam dependências.
- Confira erros de execução e avisos antes de reportar resultados.
- Diferencie problemas do site, das ferramentas e da rede.
- Auditorias locais não comprovam indexação, ranking
  ou funcionamento de serviços externos.

## Entrega
Apresente problemas encontrados, verificações executadas
e validações manuais pendentes.
Não envie mensagens de WhatsApp nem publique sem autorização.
