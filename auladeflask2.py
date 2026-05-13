from flask import Flask

app = Flask(__name__)

@app.route('/')
def exibir():
    return '''
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Meu Currículo Profissional</title>
    <style>
        body { font-family: Arial, sans-serif; line-height: 1.6; margin: 20px; color: #333; }
        .container { max-width: 800px; margin: auto; border: 1px solid #ddd; padding: 20px; }
        header { text-align: center; border-bottom: 2px solid #333; padding-bottom: 10px; }
        h1 { margin: 0; }
        h2 { color: #0056b3; border-bottom: 1px solid #ccc; }
        .contact-info { font-size: 0.9em; color: #555; }
        .experience-item, .education-item { margin-bottom: 15px; }
        .job-title { font-weight: bold; }
        .date { font-style: italic; color: #777; }
    </style>
</head>
<body>

<div class="container">
    <header>
        <h1>Seu Nome Completo</h1>
        <p class="contact-info">
            Email: seuemail@email.com | Telefone: (11) 99999-9999<br>
            LinkedIn: ://linkedin.com | Cidade - Estado
        </p>
    </header>

    <section id="sobre">
        <h2>Sobre Mim</h2>
        <p>Profissional dedicado com experiência na área de [Sua Área]. Busco novas oportunidades para aplicar meus conhecimentos em [Habilidade 1] e [Habilidade 2], contribuindo para o crescimento da empresa.</p>
    </section>

    <section id="experiencia">
        <h2>Experiência Profissional</h2>
        <div class="experience-item">
            <p class="job-title">Cargo - Empresa | <span class="date">Janeiro 2020 - Atual</span></p>
            <ul>
                <li>Responsável pela gestão de projetos e equipes.</li>
                <li>Implementação de novas tecnologias para aumentar a produtividade.</li>
            </ul>
        </div>
        <div class="experience-item">
            <p class="job-title">Cargo Anterior - Empresa B | <span class="date">Junho 2017 - Dezembro 2019</span></p>
            <ul>
                <li>Suporte técnico ao cliente e manutenção de sistemas.</li>
            </ul>
        </div>
    </section>

    <section id="educacao">
        <h2>Educação</h2>
        <div class="education-item">
            <p><strong>Nome da Instituição</strong> - Curso de Graduação | <span class="date">2013 - 2017</span></p>
        </div>
    </section>

    <section id="habilidades">
        <h2>Habilidades</h2>
        <ul>
            <li>Habilidade Técnica 1 (ex: HTML/CSS)</li>
            <li>Habilidade Técnica 2 (ex: Gestão de Projetos)</li>
            <li>Ferramenta/Software (ex: Excel Avançado)</li>
        </ul>
    </section>
</div>

</body>
</html>
'''

if __name__ == '__main__':
    app.run(debug=True)