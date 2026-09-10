from flask import Blueprint, redirect

menu_bp = Blueprint('menu', __name__)

EXTERNAL_ROUTES = {
    'open_finance': 'https://www.bb.com.br/site/open-finance/',
    'sobre_nos': 'https://www.bb.com.br/site/sobre-nos/#/',
    'minha_privacidade': 'https://www.bb.com.br/site/pra-voce/seguranca/minha-privacidade/',
    'imprensa': 'https://imprensa.bb.com.br/',
    'relacoes_investidores': 'https://ri.bb.com.br/',
    'imoveis': 'https://www.bb.com.br/site/compras-contratacao-e-venda-de-imoveis/',
    'sustentabilidade': 'https://www.bb.com.br/site/sustentabilidade/como-bb-atua/',
    'analises_investimentos': 'https://www.bb.com.br/site/investimentos/analises/',
    'facebook': 'https://www.facebook.com/bancodobrasil',
    'instagram': 'https://www.instagram.com/bancodobrasil/',
    'x': 'https://x.com/bancodobrasil',
    'youtube': 'https://www.youtube.com/bancodobrasil',
    'linkedin': 'https://www.linkedin.com/company/bancodobrasil/',
    'spotify': 'https://open.spotify.com/user/bancodobrasil',
    'tiktok': 'https://www.tiktok.com/@bancodobrasil',
    'twitch': 'https://www.twitch.tv/bancodobrasil',
    'ativos_bb': 'https://ativosbb.com.br/quem-somos',
    'bb_asset': 'https://www.bbasset.com.br/',
    'bb_corretora': 'https://www.bb.com.br/site/sobre-nos/entidades-ligadas-ao-banco-do-brasil/bb-corretora-de-seguros-e-administradora-de-bens/',
    'bb_consorcios': 'https://www.bb.com.br/site/sobre-nos/entidades-ligadas-ao-banco-do-brasil/bb-consorcios/',
    'bb_previdencia': 'https://bbprevidencia.com.br/',
    'bb_seguros': 'https://www.bb.com.br/site/sobre-nos/entidades-ligadas-ao-banco-do-brasil/bb-seguros/',
    'bb_seguros_site': 'https://www.bbseguros.com.br/',
    'blog_bb': 'https://blog.bb.com.br/?utm_source=portalbb&utm_medium=testeiraVoce&utm_campaign=2021_experimentoblogbb&utm_term=mnm&utm_content=inst_geral_serv_br_organico',
    'acesso_a_informacao': 'https://www.bb.com.br/site/acesso-a-informacao/',
    'transparencia': 'https://www.bb.com.br/site/portal-da-transparencia/',
    'declaracao_acessibilidade': 'https://www.bb.com.br/site/declaracao-de-acessibilidade/',
    'reforma_tributaria': 'https://www.bb.com.br/site/reforma-tributaria/'
}

# Rotas do Menu (O BB)
@menu_bp.route('/o-bb/open-finance')
def r_open_finance(): return redirect(EXTERNAL_ROUTES['open_finance'], code=302)

@menu_bp.route('/o-bb/sobre-nos')
def r_sobre_nos(): return redirect(EXTERNAL_ROUTES['sobre_nos'], code=302)

@menu_bp.route('/o-bb/minha-privacidade')
def r_privacidade(): return redirect(EXTERNAL_ROUTES['minha_privacidade'], code=302)

@menu_bp.route('/o-bb/imprensa')
def r_imprensa(): return redirect(EXTERNAL_ROUTES['imprensa'], code=302)

@menu_bp.route('/o-bb/relacoes-com-investidores')
def r_ri(): return redirect(EXTERNAL_ROUTES['relacoes_investidores'], code=302)

@menu_bp.route('/o-bb/imoveis')
def r_imoveis(): return redirect(EXTERNAL_ROUTES['imoveis'], code=302)

@menu_bp.route('/o-bb/sustentabilidade')
def r_sustentabilidade(): return redirect(EXTERNAL_ROUTES['sustentabilidade'], code=302)

@menu_bp.route('/o-bb/analises-de-investimentos')
def r_analises(): return redirect(EXTERNAL_ROUTES['analises_investimentos'], code=302)

# Rotas do Menu (Redes Sociais)
@menu_bp.route('/redes-sociais/facebook')
def r_face(): return redirect(EXTERNAL_ROUTES['facebook'], code=302)

@menu_bp.route('/redes-sociais/instagram')
def r_insta(): return redirect(EXTERNAL_ROUTES['instagram'], code=302)

@menu_bp.route('/redes-sociais/x')
def r_x(): return redirect(EXTERNAL_ROUTES['x'], code=302)

@menu_bp.route('/redes-sociais/youtube')
def r_yt(): return redirect(EXTERNAL_ROUTES['youtube'], code=302)

@menu_bp.route('/redes-sociais/linkedin')
def r_li(): return redirect(EXTERNAL_ROUTES['linkedin'], code=302)

@menu_bp.route('/redes-sociais/spotify')
def r_spo(): return redirect(EXTERNAL_ROUTES['spotify'], code=302)

@menu_bp.route('/redes-sociais/tiktok')
def r_tik(): return redirect(EXTERNAL_ROUTES['tiktok'], code=302)

@menu_bp.route('/redes-sociais/twitch')
def r_twi(): return redirect(EXTERNAL_ROUTES['twitch'], code=302)

# Rotas do Menu (Empresas Coligadas)
@menu_bp.route('/empresas-coligadas/ativos-bb')
def r_ativos(): return redirect(EXTERNAL_ROUTES['ativos_bb'], code=302)

@menu_bp.route('/empresas-coligadas/bb-asset')
def r_asset(): return redirect(EXTERNAL_ROUTES['bb_asset'], code=302)

@menu_bp.route('/empresas-coligadas/bb-corretora')
def r_corretora(): return redirect(EXTERNAL_ROUTES['bb_corretora'], code=302)

@menu_bp.route('/empresas-coligadas/bb-consorcios')
def r_consorcios(): return redirect(EXTERNAL_ROUTES['bb_consorcios'], code=302)

@menu_bp.route('/empresas-coligadas/bb-previdencia')
def r_prev(): return redirect(EXTERNAL_ROUTES['bb_previdencia'], code=302)

@menu_bp.route('/empresas-coligadas/bb-seguros')
def r_seguros(): return redirect(EXTERNAL_ROUTES['seguros'], code=302)

@menu_bp.route('/empresas-coligadas/bb-seguros-site')
def r_seguros_site(): return redirect(EXTERNAL_ROUTES['bb_seguros_site'], code=302)

# Rotas do Menu (Outras opções)
@menu_bp.route('/blog-bb')
def r_blog(): return redirect(EXTERNAL_ROUTES['blog_bb'], code=302)

@menu_bp.route('/acesso-a-informacao')
def r_acesso(): return redirect(EXTERNAL_ROUTES['acesso_a_informacao'], code=302)

@menu_bp.route('/transparencia')
def r_transp(): return redirect(EXTERNAL_ROUTES['transparencia'], code=302)

@menu_bp.route('/declaracao-de-acessibilidade')
def r_acess(): return redirect(EXTERNAL_ROUTES['declaracao_acessibilidade'], code=302)

@menu_bp.route('/reforma-tributaria')
def r_reforma(): return redirect(EXTERNAL_ROUTES['reforma_tributaria'], code=302)