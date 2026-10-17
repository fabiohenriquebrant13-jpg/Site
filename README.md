# Ferreira Motores — site institucional

Site em HTML, CSS e JavaScript para a Ferreira Motores, com conteúdo em português
brasileiro e endereço oficial informado: https://www.ferreiramotores.com.br/.

## Arquivos e publicação

- `index.html` + `assets/`: versão recomendada para publicar na Hostinger.
- `ferreira-motores-completo.html`: versão independente com imagens incorporadas,
  útil para abrir ou compartilhar um único arquivo.
- `Ferreira-Motores-Site-v2.zip`: pacote publicável, com `index.html` na raiz e
  somente os assets locais referenciados. Extraia em `public_html` do domínio,
  preservando uma cópia dos arquivos anteriores antes da substituição.
- `.agents/skills/`: instruções de desenvolvimento; não fazem parte da publicação.
- `AGENTS.md` e `memoria/README.md`: regras do projeto e decisões registradas.

Para visualizar localmente, da raiz do projeto:

```bash
python3 -m http.server 8000 --directory .
```

## Imagens e contraste restaurados — 17/10/2026

A pedido do usuário, as 14 imagens, os dois fundos dos cartões de serviços e o
respectivo gradiente voltaram à versão anterior às otimizações. O site usa os
arquivos originais de `assets/`, sem `srcset` das variantes recomprimidas.
Os ajustes de layout, a galeria por teclado, os metadados e as skills permanecem.
Os horários continuam somente na tabela amarela ao final de Fale conosco.

As duas versões HTML e o ZIP foram sincronizados. O HTML independente conserva
a deduplicação dos fundos incorporados; o ZIP inclui somente os 20 arquivos
referenciados (index e 19 assets). As variantes em `assets/responsive/` e seu
gerador permanecem disponíveis, mas não são utilizadas na versão restaurada.
Em futuras otimizações, preserve a qualidade e o contraste visual aprovados.

Validação local: ambos os HTMLs passaram nas 130 verificações funcionais em
320, 375, 768 e 1440 pixels. O ZIP extraído também foi conferido. A ferramenta
de acessibilidade não detectou violações automáticas; contraste sobre imagens
continua exigindo revisão manual.

As notas abaixo pertencem à versão otimizada anterior e **não representam esta
versão restaurada**. Não foi realizada uma nova medição de Lighthouse.

## Histórico das otimizações anteriores — 17/10/2026

Este registro descreve a versão anterior à restauração acima.


- Criadas 30 variantes WebP em `assets/responsive/`, mantendo os originais.
  Os `<img>` da versão publicada usam `srcset` e `sizes` para a seleção adequada
  ao tamanho da tela. A imagem principal continua com prioridade de carregamento.
- Fundos dos dois cartões de serviço usam variantes menores. O gradiente sob
  os textos ficou mais escuro para manter contraste sobre as fotografias.
- Entre 621 e 1100 pixels, o texto da apresentação fica separado do motor e da
  faixa amarela. No computador maior, o parágrafo tem largura limitada para
  evitar contato com a imagem; a composição do celular foi preservada.
- O HTML independente usava as imagens de fallback otimizadas e compartilha os
  fundos incorporados por variáveis CSS, evitando duplicação de dados.
  Passou de 1.706.546 para 1.057.241 bytes: redução de 38%.
- O ZIP foi refeito com 48 arquivos necessários à página. A seleção de assets
  inclui as versões responsivas e os originais usados como opção de alta resolução;
  ferramentas, skills, relatórios e imagens sem referência ficam fora do pacote.

### Notas de desempenho /100 — Lighthouse 13.5.0 local

| Versão | Cenário | Antes | Depois |
|---|---|---:|---:|
| Principal | Celular | 99 | 99 |
| Principal | Computador | 100 | 100 |
| Independente | Celular | 57 | 63 |
| Independente | Computador | 88 | 96 |

Acessibilidade automática, boas práticas e SEO mantiveram 100/100 nas quatro
execuções posteriores. No HTML principal, os dados transferidos na medição móvel
caíram de 313.039 para 230.144 bytes (26%) e, no computador, de 589.015 para
293.679 bytes (50%). LCP móvel: 2,1 s → 1,8 s. No independente: 9,1 s → 6,0 s.

São execuções únicas por cenário, em servidor HTTP local sem compressão, com a
mesma versão do Lighthouse, modos simulados mobile/desktop e serviços externos
bloqueados. As notas não medem Hostinger, abertura por `file://`, indexação ou
ranking. O independente continua mais pesado na carga inicial; prefira a versão
principal para publicação.

Evidências resumidas, cenários e hashes dos arquivos avaliados:
[memoria/otimizacoes-2026-10-17.json](memoria/otimizacoes-2026-10-17.json).

### Validação funcional e contraste

- Checklist funcional: 100/100 calculado, com 18/18 critérios e 130 verificações
  nos dois HTMLs em 320, 375, 768 e 1440 pixels. Pesos: aprovado 1, aviso 0,5,
  falha 0; nota = 100 × pontos / critérios avaliados.
- Menu, Escape, galeria por teclado, FAQ, imagens, âncoras, metadados e a tabela
  amarela de horários ao final de Fale conosco foram preservados.
- axe-core: nenhuma violação automática detectada nas oito execuções; alguns
  resultados de contraste sobre imagens continuam inconclusivos para a ferramenta.
- Revisão adicional de contraste: fundos escuros/cores da apresentação e textos
  dos cartões conferidos por amostragem e por limite conservador de gradiente;
  sobreposição na faixa de tablet eliminada. Isso não comprova conformidade WCAG
  completa nem substitui testes com leitores de tela e navegadores reais.

## Regenerar as versões

Os geradores usam Python 3.9 ou superior, somente com a biblioteca padrão:

```bash
python3 scripts/build-standalone.py
python3 scripts/build-package.py
```

O HTML independente é gerado a partir do `index.html`; não edite somente a cópia
incorporada. O ZIP deve ser refeito quando uma alteração aprovada precisar ser
levada à hospedagem.

Opcional: para recriar as variantes antigas, use Node.js compatível e Sharp 0.35.5 como
ferramenta de desenvolvimento, fora das dependências do site:

```bash
npm install --prefix /tmp/ferreira-image-tools sharp@0.35.5
NODE_PATH=/tmp/ferreira-image-tools/node_modules node scripts/optimize-images.cjs
python3 scripts/build-standalone.py
python3 scripts/build-package.py
```

Essas variantes não são aplicadas automaticamente pelo gerador de imagens.
A geração de WebP usa qualidade 82 (logo: 90), effort 6 e não amplia imagens.
Confirme qualidade visual, carregamento e comportamento antes de publicar.
Resultados antigos de auditoria não validam automaticamente uma nova versão.
