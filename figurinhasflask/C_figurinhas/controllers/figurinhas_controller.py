from flask import Blueprint, redirect, render_template, request, url_for

from models import Colecionador, Figurinha, ItemOferta, OfertaTroca, db

# Apelido "figurinhas" → use url_for('figurinhas.index') nos templates
figurinhas_bp = Blueprint("figurinhas", __name__, url_prefix="/figurinhas")


@figurinhas_bp.route("/")
def index():
    return render_template(
        "figurinhas/lista_ofertas.html", 
        ofertas=OfertaTroca.listar_com_colecionador()
    )


@figurinhas_bp.route("/oferta/cadastrar", methods=["GET", "POST"])
def cadastrar_oferta():
    colecionadores = Colecionador.listar()
    figurinhas = Figurinha.listar()

    if request.method == "POST":
        # 1. Coleta os dados básicos da oferta vindos do formulário
        colecionador_id = request.form.get("colecionador_id")
        observacao = request.form.get("observacao")

        # 2. Cria a instância principal da Oferta de Troca
        nova_oferta = OfertaTroca(
            colecionador_id=colecionador_id,
            observacao=observacao
        )
        
        # Adiciona ao banco para gerar o ID da oferta antes de criar os itens
        db.session.add(nova_oferta)
        db.session.flush()  # Garante o ID sem commitar a transação inteira ainda

        # 3. Coleta os dados dos itens (Figurinha que OFERECE)
        figurinha_oferece_id = request.form.get("figurinha_oferece_id")
        qtd_oferece = request.form.get("qtd_oferece", 1, type=int)

        if figurinha_oferece_id:
            item_oferece = ItemOferta(
                oferta_id=nova_oferta.id,
                figurinha_id=figurinha_oferece_id,
                tipo="oferece",
                quantidade=qtd_oferece
            )
            db.session.add(item_oferece)

        # 4. Coleta os dados dos itens (Figurinha que DESEJA)
        figurinha_deseja_id = request.form.get("figurinha_deseja_id")
        qtd_deseja = request.form.get("qtd_deseja", 1, type=int)

        if figurinha_deseja_id:
            item_deseja = ItemOferta(
                oferta_id=nova_oferta.id,
                figurinha_id=figurinha_deseja_id,
                tipo="deseja",
                quantidade=qtd_deseja
            )
            db.session.add(item_deseja)

        # 5. Salva todas as alterações no banco de dados com segurança
        try:
            db.session.commit()
            return redirect(url_for("figurinhas.index"))
        except Exception as e:
            db.session.rollback()
            # Opcional: Adicionar uma mensagem de erro em flash aqui se desejar
            print(f"Erro ao salvar a oferta: {e}")

    return render_template(
        "figurinhas/formulario_oferta.html",
        colecionadores=colecionadores,
        figurinhas=figurinhas,
    )