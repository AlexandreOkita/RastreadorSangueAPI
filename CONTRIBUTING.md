# Como contribuir

Caso você deseje contribuir de outras formas além do código, confira [essa seção](#outras-formas-de-contribuir).

## Contribuindo com código

Esse documento traz uma visão passo a passo para pessoas que estão contribuindo pela primeira vez em um projeto open source. Caso não seja seu caso, mas você deseja entender mais como contribuir para o projeto, veja a seção [Adicionando um novo hospital](#adicionando-um-novo-hospital)

### Primeiro passo - Fazer o Fork do repositório:

Faça o Fork deste repositório e clone o seu novo repositório forked para a sua máquina.

Para fazer o Fork do repositório, você encontrará um botão escrito `fork` no topo desta página. Para clonar o seu repositório forked, clique no botão verde escrito `Code` e copie a URL https (se preferir, você também pode usar ssh para cloná-lo). O link será algo como: `https://github.com/SEU-USUARIO/RastreadorSangueAPI.git`.

### Segundo passo - Enviar a sua contribuição:

Agora é hora de fazer a sua contribuição! Mas antes de fazer isso, crie uma nova branch e mude para ela usando o seguinte comando: `git checkout -b [NOME-DA-BRANCH]`. Geralmente, o nome da branch dá a ideia do que você quer implementar no código. Caso você esteja adicionando um novo hospital no banco, uma sugestão é utilizar o padrão ```new/nome_hospital```.

#### Adicionando um novo hospital

A ideia do projeto é que sejam criados diversos crawlers que serão executados em cima de lambdas diariamente e que irão alimentar um banco de dados que é consumido pela API. Desse modo, para adicionar um novo hospital na base há 4 passos que podem ser seguidos:
    
1. Procurar um hospital que publique de algum modo o estado dos estoques de sangue. Essa publicação normalmente é feita diretamente em um site como no [exemplo](https://www.prosangue.sp.gov.br/home/).
2. Criar uma função que consiga obter esses dados e que os adicione na tabela DynamoDB que é consumida pela API (a estrutura de diretórios sugerida é ```hospitals/{nome_hospital}/{nome_hospital_crawler_function}/app.py```). Para saber mais sobre a estrutura da tabela, veja a seção logo após essa. Um exemplo pode ser visto nesse [arquivo](hospitals/hc_unicamp/hc_unicamp_crawler_function/hc_unicamp_blood_status/app.py) (o arquivo está em python mas sita-se livre para utilizar qualquer linguagem suportada pela Lambda).
3. Criar o arquivo ```template.yaml``` da sua função. Esse arquivo cria a lambda que será responsável por executar seu código diariamente. Um exemplo para ser seguido pode ser encontrado [aqui](hospitals/hc_unicamp/template.yaml) 
4. Adicionar a nova lambda no arquivo [hospital_lambdas.yaml](hospitals/hospital_lambdas.yaml). Adicione um novo resource com o nome da sua função com a nova Location (não esqueça de mudar o nome do recurso).

#### Estrutura dos dados

Os dados são estruturados em uma tabela NoSQL da seguinte forma:
- **Chave de partição**: ```hospital```
  - Contém o nome do hospital. Esse nome deve ser único e serve como um identificador.
- **Chave de classificação**: ```date```
  - Contém a data da inserção do dado na tabela. Serve para ordenar os dados durante a utilização da API. Não deve existir dois dados contendo o mesmo valor na chave de partição e de classificação.
- **Outros atributos**: Todos os seguintes atributos possuem apenas os valores ```stable```, ```alert``` e ```critic```. Esses atributos trazem o status de cada tipo sanguíneo no hospital em uma determinada data.
  - ```a_minus_status```
  - ```a_plus_status```
  - ```b_minus_status```
  - ```b_plus_status```
  - ```o_minus_status```
  - ```o_plus_status```
  - ```ab_minus_status```
  - ```ab_plus_status```
#### Fazendo o commit

Depois de ter feito a sua contribuição, **é hora de fazer o commit!**

Execute os seguintes comandos:

- `git status` - este comando mostrará todas as suas modificações
- `git add [ARQUIVO]` - este comando adicionará o arquivo modificado. Você pode adicionar todos os arquivos modificados em um diretório usando `git add .`
- `git status` - verifique se todas as suas modificações foram adicionadas
- `git commit -m "[MENSAGEM]"` - este comando criará o seu commit! Crie-o com uma descrição curta (geralmente com menos de 50 caracteres) das suas alterações
- `git push origin [NOME-DA-SUA-BRANCH]` - este comando enviará as suas modificações para o seu repositório forked no GitHub

### Terceiro passo - Criar o seu PR:

Depois de ter enviado o seu commit, você verá um botão verde `Compare & pull request` no topo da página do seu repositório forked (se você não vê-lo, crie o PR clicando no botão Pull Requests).

Confirme no topo da página, se você está fazendo o merge para o repositório original em `base fork`.

---

## Outras formas de contribuir

Há várias outras formas de contribuir com o projeto sem necessitar de código! Algumas ideias são listadas abaixo:

### Sugerindo um novo hospital

Caso você conheça um hemocentro que ainda não está na base, crie uma issue no repositório com o link do site em que é possível obter o status do estoque de sangue.

### Ajudando na documentação

O projeto ainda é super novo e qualquer ajuda na documentação para torná-lo mais orgazinado é super bem vinda!

### Divulgando :)

Divulgar o projeto é uma ótima forma de contribuir, pois assim podemos encontrar novas pessoas e continuar crescendo o nosso banco!
