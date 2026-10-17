# Avaliações com notas de 0 a 100

Preferência do usuário: apresentar avaliações mensuráveis, como a de SEO, com
notas de 0 a 100 conforme o tipo de avaliação e a capacidade da skill.

## Notas fornecidas por ferramentas

- Use a nota real da execução atual e identifique ferramenta, categoria, arquivo
  ou URL, data e cenário. Separe celular e computador quando houver medições.
- Converta escalas somente de forma explícita: uma nota Lighthouse entre 0 e 1
  pode ser multiplicada por 100. Não substitua a fórmula original da ferramenta.
- Não reutilize notas antigas como resultado de uma nova versão. Quando forem
  citadas para comparação, identifique versão e cenário anteriores.
- Não derive uma nota geral por média entre categorias diferentes sem um método
  definido que justifique essa agregação.

## Skills que só produzem checklist ou achados

- Preserve também o resultado original: aprovado, aviso, falha, erro, não aplicável
  ou não executado. Não chame um índice calculado de nota oficial da ferramenta.
- Quando for útil fornecer uma nota, defina os critérios aplicáveis antes de
  avaliar. Use critérios verificáveis, sem dividir artificialmente um problema
  em vários itens para alterar o resultado.
- Se a skill não estabelecer uma rubrica própria, use pesos iguais: aprovado = 1,
  aviso = 0,5 e falha = 0. A nota do checklist é:

  nota = 100 × soma dos pontos dos itens avaliados / quantidade de itens avaliados

- Erros de ferramenta ou acesso e itens não executados não recebem zero e não
  contam como aprovados. Itens não aplicáveis ficam fora do escopo.
- Informe a cobertura: itens avaliados / itens aplicáveis. Se faltar algum item
  aplicável, rotule a nota como parcial. Sem itens avaliados, não calcule nota.
- Apresente esse resultado como "índice do checklist, calculado", com a rubrica,
  cobertura e achados. Um resultado alto não deve esconder um problema crítico.
- Avaliações visuais ou qualitativas exigem critérios explícitos; não invente uma
  nota apenas para completar uma tabela.

## Formato da entrega

Use uma tabela curta quando ajudar a comparar:

| Categoria | Nota /100 | Origem e cenário | Cobertura e limites |
|---|---|---|---|
| Categoria medida | Resultado real | Ferramenta, versão e cenário | Limitações da execução |
| Checklist | Resultado calculado | Rubrica identificada | Itens avaliados/aplicáveis; parcial se necessário |
| Categoria não executada | Não avaliado | Motivo | Sem nota inventada |

Explique as falhas e próximas ações prioritárias. Quando houver antes/depois,
compare o mesmo cenário, ferramenta e critérios; sinalize mudanças de escopo
que impeçam comparação direta. Não confunda nota de laboratório com ranking,
indexação, conformidade WCAG completa ou garantia de desempenho em produção.

Ao salvar relatórios, inclua notas, evidências e limitações. Esta preferência é
sobre as avaliações enviadas ao usuário; não inclui colocar notas na página
pública do site sem um pedido específico.
