# Exemplos de uso e portabilidade

## Neste projeto

Abra uma nova tarefa na branch que contém a skill e peça:

> Use $melhorar-html para melhorar a navegação da galeria no celular, preservando o visual.

> Use $melhorar-html para revisar o site. Primeiro apresente problemas e recomendações, sem alterar o HTML.

> Use $melhorar-html para deixar a seção de contato mais legível. Atualize também a versão independente e o ZIP e salve na branch que indiquei.

As skills específicas e os AGENTS.md do projeto fornecem informações como marca,
idioma, arquivos principais e decisões aprovadas. Esta skill não embute esses dados
para permitir reutilização.

## Em outro projeto

1. Copie a pasta inteira `melhorar-html`, com `SKILL.md` e `references/`, para
   `.agents/skills/` do outro repositório.
2. Preserve os caminhos internos. A pasta deve resultar em
   `.agents/skills/melhorar-html/SKILL.md`, sem um nível duplicado.
3. Inicie uma nova tarefa/sessão selecionando o projeto e a branch corretos.
4. Peça: "Use $melhorar-html para melhorar esta página", explicando o objetivo.

Não é preciso copiar o site original, ZIP de hospedagem, bibliotecas de templates,
credenciais ou os demais arquivos deste repositório. Esta skill contém instruções
e referências; não instala ferramentas automaticamente nem altera um site ao ser
copiada. A descoberta automática depende do cliente e da nova sessão.

## Cenários para conferir o comportamento

- **Somente auditoria:** deve gerar recomendações, sem editar a aplicação.
- **Correção localizada:** deve resolver o problema e conferir a regressão, sem
  redesenhar partes aprovadas que não pertencem ao pedido.
- **Domínio ausente:** deve concluir melhorias independentes e pedir o endereço
  antes de inserir canonical ou URLs oficiais.
- **Projeto com build:** deve usar a fonte e os comandos do projeto, respeitando
  seu framework, em vez de editar apenas o HTML compilado.
- **ZIP autorizado:** deve testar o conteúdo extraído; não apenas o arquivo fonte.
- **Ferramenta ausente:** deve localizar ou preparar o necessário, informar o que
  permaneceu sem teste e nunca declarar uma nota ou conformidade não medida.

## Origem

Skill original criada para este pedido. Os ZIPs Publii e Ant Design Landing são
projetos de aplicações/templates e não contêm esta skill. Nenhum código desses
pacotes foi incorporado à skill ou ao HTML do site.
