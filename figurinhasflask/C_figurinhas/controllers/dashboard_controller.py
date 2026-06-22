from flask import Blueprint, render_template
from models import Colecionador, Figurinha, OfertaTroca

dashboard_bp = Blueprint("dashboard", __name__)

@dashboard_bp.route("/")
def index():
    # Contagem total de registros para exibir no painel
    total_colecionadores = len(Colecionador.listar())
    total_figurinhas = len(Figurinha.listar())
    total_ofertas = len(OfertaTroca.listar_com_colecionador())

    return render_template(
        "index.html",
        total_colecionadores=total_colecionadores,
        total_figurinhas=total_figurinhas,
        total_ofertas=total_ofertas
    )