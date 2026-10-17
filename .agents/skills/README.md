# Skills de desenvolvimento deste projeto

## Melhorar HTML — reutilizável

A skill `melhorar-html` foi criada para orientar melhorias em páginas HTML, CSS e
JavaScript deste projeto e de futuros sites. Cobre layout, responsividade,
acessibilidade, metadados, desempenho e validação, respeitando as instruções locais.

- Instruções: [melhorar-html/SKILL.md](melhorar-html/SKILL.md).
- Checklist: [melhorar-html/references/checklist.md](melhorar-html/references/checklist.md).
- Uso e instalação em outros projetos: [exemplos](melhorar-html/references/exemplos.md).
- Não exige pacotes por si só; usa as ferramentas que o projeto tiver ou precisar.
- Para reutilizar, copie a pasta inteira `melhorar-html` para `.agents/skills/`
  do outro repositório e inicie uma nova sessão/tarefa nesse projeto.

Exemplo de pedido:

> Use $melhorar-html para melhorar a seção de contato no celular, preservando a identidade visual.

A skill é original e foi criada para este pedido. `Publii-master.zip` e
`ant-design-landing-master.zip` contêm aplicações/templates, sem `SKILL.md`.
Esses arquivos foram preservados; seus códigos não foram importados para o site.

## Skills de SEO

As skills `seo-audit` e `seo-audit-full` foram instaladas a partir do ZIP enviado
na branch `readme-edits`. O ZIP original foi removido após a instalação. Fazer merge desta
branch leva as pastas instaladas à `main`; somente enviar um ZIP não instala skills.

## Organização

- `seo-audit/SKILL.md`: instruções da auditoria básica.
- `seo-audit-full/SKILL.md`: instruções da auditoria completa.
- Cada skill conserva seus próprios `scripts/`, `references/` e `assets/`.
- Cada pasta inclui a licença MIT do autor. Os arquivos extraídos não foram modificados.
- As imagens e os modelos das skills não devem ser misturados com `assets/` do site.
- Estas pastas são ferramentas de desenvolvimento e não entram no ZIP da Hostinger.

## Dependência Python

O ambiente cloud atual já está preparado. Em um ambiente novo, execute da raiz
do repositório (`/workspace/Site` neste ambiente):

```bash
python3 -m venv /workspace/seo-audit-tools/venv
/workspace/seo-audit-tools/venv/bin/python -m pip install -r .agents/skills/requirements-seo-audit.txt
```

O ambiente virtual fica fora do repositório. O arquivo de requisitos registra
as versões instaladas e verificadas, incluindo `requests==2.34.2`.
Não é necessário instalar nada no seu computador para usar as skills aqui.

## Usar no Codex

1. Abra uma nova tarefa/sessão com a branch `readme-edits` selecionada, ou use
   `main` depois de integrar esta branch.
2. Peça, por exemplo: "Use a skill seo-audit para analisar https://SEU-DOMINIO/".
3. O agente deve ler o `SKILL.md`, usar o Python do ambiente virtual acima e
   seguir os caminhos relativos da pasta da skill.
4. A skill produz um relatório HTML em `reports/`. A auditoria, por si só,
   não altera nem publica o site.

Para conferir apenas o validador local de dados estruturados:

```bash
/workspace/seo-audit-tools/venv/bin/python .agents/skills/seo-audit/scripts/check-schema.py --file index.html
```

A versão `seo-audit-full` exige uma chave Google PageSpeed Insights para uma
auditoria completa. Configure-a de forma segura como `PAGESPEED_API_KEY` ou
`GOOGLE_PAGESPEED_API_KEY` no ambiente; não coloque valores em commits ou no chat.
A instalação e os validadores locais não precisam dessa chave. Acesso aos domínios
analisados e aos serviços externos também depende da política de rede do ambiente.

## Validação inicial da instalação

- Os dez scripts responderam a `--help` sem erro de dependências.
- Os dois validadores JSON-LD analisaram `index.html`: `pass`, dois blocos JSON-LD.
- O validador de metadados sociais executou e retornou `warn`; isso é um achado
  sobre os metadados atuais do site, não uma falha de instalação.
- `pip check`: nenhuma dependência quebrada.
- Não foi executada uma auditoria completa, nem verificada a descoberta automática
  das skills em uma nova sessão.

## Origem e licença

- Projeto informado pelo pacote: https://github.com/JeffLi1993/seo-audit-skill
- Arquivo original: `seo-audit-skill-main.zip`, adicionado no commit `0e290b0`.
- SHA-256: `cddccab0ab2b2919a468c3c5e58e9760303c4942d79a37793a6d9a1ade4c87ea`.
- Licença MIT, Copyright (c) 2026 Jeff; veja `LICENSE` em cada pasta.
