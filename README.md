# O fim do software de escritório

[![O fim do software de escritório](guia/assets/banner.jpg)](https://inematds.github.io/o-fim-do-software-de-escritorio/guia/)

**[Português](README.md) · [English](README.en.md) · [Español](README.es.md)**

## O que é

O fim do software de escritório é uma visão de Nei Maldaner sobre trabalhar com inteligência artificial a partir dos objetivos do negócio. É para profissionais, gestores e donos de empresas que gastam tempo preparando materiais, preenchendo sistemas e repetindo informações. O guia mostra como passar desse trabalho de preparação para um processo de decisão e execução acompanhada. Você encontra exemplos, um plano de transição e um kit gratuito para testar um processo com dados fictícios. Para começar, basta ler e escolher uma tarefa que você conheça bem.

## Guia e kit gratuitos

Leia o **[guia completo](https://inematds.github.io/o-fim-do-software-de-escritorio/guia/)** e baixe o **[kit](https://inematds.github.io/o-fim-do-software-de-escritorio/kit-inteligencia-operacional.zip)**.

- [Visão original de Nei Maldaner](docs/visao-original.md).
- [Pedido por resultado, exemplo e resposta esperada](kit/pedido-por-resultado.md).
- [Mapa do processo](kit/mapa-do-processo.md).
- [Medição de tempo e qualidade](kit/medir-antes-depois.csv).
- [Registro de decisão e acompanhamento](kit/decisao-e-acompanhamento.md).

## Executar o exemplo opcional

Requer Python 3.9+. Extraia o ZIP e abra o terminal na pasta que contém kit, ou execute na raiz deste repositório:

```bash
python3 kit/conferir_exemplo.py
```

Windows: `py -3 kit/conferir_exemplo.py`. Sem Python, siga a conferência manual no guia.

Esperado: C001 (76 dias) e C004 (46 dias), duplicidade C004 e data ausente C003. Zero mensagens enviadas. **Conferidor determinístico, sem IA ou rede.** Para usar IA, copie o pedido e anexe o CSV na conversa de uma ferramenta que você já utiliza. Nenhum ganho de produtividade empresarial foi medido.

## Vídeo

Explicavideo com o avatar de Nei Maldaner em produção para lives11. O link será inserido aqui e no guia quando publicado.

## Autoria e fontes

Tese de Nei Maldaner; conteúdo educacional aberto. Falências e redução de equipes são cenários, não previsões garantidas. [OIT (2025)](https://www.ilo.org/publications/generative-ai-and-jobs-refined-global-index-occupational-exposure) · [Microsoft Work IQ](https://www.microsoft.com/en-us/copilot/features/work-iq).

## Manutenção

O conteúdo PT está em docs/guia-completo.md. `python3 scripts/gerar_guia.py` usa o template INEMA preservado e requer o pacote Python markdown. Traduções: inema-traduz pela assinatura. A geração do guia substitui o HTML PT; preserve qualquer embed de vídeo que já tiver sido publicado. Publicação via git/GitHub Pages.
