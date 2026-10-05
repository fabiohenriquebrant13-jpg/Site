---
name: ferreira-frontend
description: Melhorar o frontend da Ferreira Motores, preservando sua identidade visual e adaptando aparência e navegação ao celular.
---

# Frontend da Ferreira Motores

## Quando usar
Use para alterações de layout, aparência, navegação e responsividade.

## Preparação
- Leia as instruções AGENTS.md aplicáveis.
- Use o checkout existente; não crie worktrees sem pedido.
- Localize index.html e assets/.
- Se o projeto estiver apenas em ZIP, prepare uma cópia de trabalho
  sem sobrescrever arquivos existentes.
- Não substitua ou recompacte o ZIP sem pedido.
- Informe quando as alterações estiverem fora dos arquivos versionados.

## Identidade e conteúdo
- Preserve amarelo, preto, branco, logo e fotografias reais.
- Use português brasileiro.
- Mantenha o foco em motores elétricos, motobombas e peças,
  em Santa Luzia/MG e região.
- Preserve contatos, endereço e horários.
- Não invente preços, garantias, avaliações, certificações
  ou vínculos com fabricantes.

## Desenvolvimento
- Prefira HTML, CSS e JavaScript simples.
- Adicione dependências apenas quando necessárias ao pedido.
- Priorize textos legíveis e botões fáceis de tocar.
- Evite rolagem horizontal indesejada na página.
- Preserve a rolagem horizontal intencional da galeria móvel.
- Mantenha imagens proporcionais e caminhos válidos.
- Preserve foco visível e navegação por teclado.

## Validação
- Confira larguras de 375, 768 e 1440 pixels.
- Teste abertura e fechamento do menu móvel.
- Confira aria-expanded, fechamento ao navegar e com Escape.
- Verifique links internos, imagens e perguntas frequentes.
- Confira os destinos de WhatsApp, telefone e mapa,
  sem enviar mensagens ou realizar chamadas.
- Use Playwright quando disponível.
- Neste ambiente, as ferramentas ficam em
  /workspace/site-dev-tools e o teste é node smoke.cjs.
- Fora deste ambiente, localize as ferramentas antes de executar.

## Entrega
Explique o que mudou, o que foi verificado e as limitações.
Não publique nem envie alterações ao GitHub sem autorização.
