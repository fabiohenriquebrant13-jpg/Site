# Checklist para melhorar HTML

Use apenas os itens pertinentes ao pedido. Marque cada verificação como aprovada,
falhou, não executada ou não aplicável. Guarde a evidência relevante e não afirme
que um item passou por suposição.

## Antes

- Branch e estado inicial registrados; alterações do usuário preservadas.
- Fonte correta localizada, incluindo gerador ou framework quando houver.
- Regras locais, identidade visual e informações comerciais identificadas.
- Objetivo verificável e área da mudança definidos.
- Domínio confirmado antes de qualquer metadado absoluto.

## Layout e conteúdo

- Celular, tablet e computador sem cortes ou sobreposições no trecho alterado.
- Sem rolagem horizontal involuntária na página inteira.
- Rolagem intencional da galeria preservada e utilizável.
- Textos, hierarquia, espaçamento e botões legíveis nas telas testadas.
- Contatos, horários e conteúdo aprovado mantidos conforme o pedido.
- Imagens existentes, proporções e tamanhos de arquivo conferidos.

## Interações

- Menu: abrir, fechar, navegar e sincronizar aria-expanded.
- Escape: fechar quando esperado e devolver foco de forma útil.
- Tab e Shift+Tab: alcançar controles sem armadilhas de foco.
- Galeria: foco visível e setas ou controles acessíveis quando houver rolagem.
- FAQ e demais controles alterados respondem ao usuário.
- Links internos resolvem; links externos têm destino conferido sem enviar nada.
- Imagens decodificam; não há recursos locais 404 nem novos erros JavaScript.
- Respeito a movimento reduzido quando houver animação.

## Semântica e metadados

- Idioma da página e hierarquia de títulos coerentes.
- Links, botões, campos e regiões têm nomes acessíveis adequados.
- Imagens informativas com alt; decorativas identificadas corretamente.
- Tabela com cabeçalhos quando usada para dados tabulares.
- Contraste e indicador de foco avaliados sobre os fundos reais.
- Título, descrição, canonical e metadados sociais coerentes com o escopo.
- Dados estruturados baseados em fatos e sintaticamente válidos, se presentes.

## Ferramentas e pacote

- Verificações existentes relevantes executadas; nada desativado para passar.
- axe-core: violações e resultados inconclusivos diferenciados, se executado.
- Lighthouse: resultados associados ao cenário medido, se executado.
- Variantes atualizadas quando exigidas pelo projeto.
- ZIP somente quando autorizado, sem arquivos internos de desenvolvimento.
- Arquivo principal no caminho exigido pela hospedagem.
- ZIP íntegro e conteúdo extraído conferido, se refeito.
- Diff final revisado; testes repetidos apenas quando uma alteração exigir.

## Entrega

- Mudança e motivo descritos com linguagem simples.
- Evidência de testes, falhas e limitações explícitas.
- Branch de destino respeitada; nenhuma publicação inferida de um commit.
- Cópia local e arquivo publicado distinguidos quando houver downloads.

- Avaliações com notas de 0 a 100 quando fundamentadas, método e cobertura
  informados; itens não avaliados identificados e notas parciais rotuladas.
