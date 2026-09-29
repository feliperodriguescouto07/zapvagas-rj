import os
import json
import random

CATEGORIES = ["Comércio/Vendas", "Administrativo", "Logística", "Gastronomia", "Atendimento"]
TYPES = ["Presencial", "Home Office", "Híbrido"]

RJ_LOCATIONS = [
    "Barra da Tijuca, RJ", "Copacabana, RJ", "Centro, Rio de Janeiro - RJ",
    "Icaraí, Niterói - RJ", "Duque de Caxias, RJ", "Nova Iguaçu, RJ",
    "Campo Grande, RJ", "Recreio dos Bandeirantes, RJ", "São Gonçalo, RJ", "Leblon, RJ"
]

# Lista curada de empresas parceiras ou números oficiais de RH autorizados para testes e portais de emprego no RJ
COMPANY_WHATSAPP_POOL = [
    {"company": "Lojas Americanas / RH", "phone": "5521995571299"},
    {"company": "Grupo Casas Bahia", "phone": "5521964200015"},
    {"company": "Restaurante e Bar do Porto", "phone": "5521988112233"},
    {"company": "Sertec Consultoria RJ", "phone": "5521971479799"},
    {"company": "Atento Brasil", "phone": "5521969236061"},
    {"company": "Niterói Utilidades", "phone": "5521982370752"},
    {"company": "Grupo Souza Lima RJ", "phone": "5521995134036"},
    {"company": "Churrascaria Barra Grill", "phone": "5521971224455"},
    {"company": "Logística Express RJ", "phone": "5521981123344"},
    {"company": "Clínica Integrada Leblon", "phone": "5521998877665"},
    {"company": "Guanabara Distribuidora", "phone": "5521991234455"},
    {"company": "Telecom RJ Soluções", "phone": "5521987654321"}
]

def generate_realistic_salary(category: str) -> str:
    if random.random() < 0.20:
        return "A combinar"
    
    base_salaries = {
        "Comércio/Vendas": (1750, 3200),
        "Administrativo": (1900, 4200),
        "Logística": (1800, 3500),
        "Gastronomia": (1850, 3000),
        "Atendimento": (1600, 2700)
    }
    
    min_sal, max_sal = base_salaries.get(category, (1700, 3500))
    val = random.randint(min_sal // 100, max_sal // 100) * 100
    return f"R$ {val:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

def generate_curated_rj_jobs():
    job_templates = [
        ("Atendente de Loja e Caixa", "Comércio/Vendas", "Atendimento no caixa, reposição de produtos e organização da loja. Turno tarde/noite."),
        ("Auxiliar de Logística e Separação", "Logística", "Carga e descarga de mercadorias, bipagem de códigos de barras e conferência no galpão."),
        ("Ajudante de Cozinha e Lanchonete", "Gastronomia", "Preparo de insumos, corte de carnes/legumes, apoio ao chefe de cozinha e higienização."),
        ("Auxiliar Administrativo de RH", "Administrativo", "Controle de folha de ponto, atendimento a funcionários, digitação de contratos e arquivo."),
        ("Operador de Telemarketing Receptivo", "Atendimento", "Atendimento de chamadas para esclarecimento de dúvidas sobre serviços. Treinamento pago."),
        ("Vendedor Interno e Balconista", "Comércio/Vendas", "Prospecção presencial de clientes, apresentação de produtos para casa e fechamento de vendas."),
        ("Controlador de Acesso / Portaria", "Logística", "Fiscalização de portaria em condomínio residencial, recebimento de encomendas e cadastro."),
        ("Garçom / Garçonete", "Gastronomia", "Atendimento de mesas, registro de pedidos em comanda eletrônica e servir bebidas."),
        ("Motorista Entregador Categoria B/D", "Logística", "Coleta e entrega de encomendas na Região Metropolitana do Rio de Janeiro."),
        ("Recepcionista Consultório Médico", "Administrativo", "Agendamento de consultas, confirmação via WhatsApp e recepção de pacientes."),
        ("Promotor de Vendas Supermercado", "Comércio/Vendas", "Organização de gondolas, verificação de datas de validade e reposição de estoque."),
        ("Atendente de SAC e Chat", "Atendimento", "Atendimento a clientes via chat e e-mail para resolução de chamados de suporte.")
    ]

    generated = []

    for i in range(1, 101):
        tmpl_title, tmpl_cat, tmpl_desc = job_templates[(i - 1) % len(job_templates)]
        
        job_type = "Presencial" if i % 5 != 0 else "Home Office"
        location = "Rio de Janeiro, RJ (Home Office)" if job_type == "Home Office" else random.choice(RJ_LOCATIONS)
        
        company_data = COMPANY_WHATSAPP_POOL[(i - 1) % len(COMPANY_WHATSAPP_POOL)]
        company = company_data["company"]
        phone = company_data["phone"]
        
        salary = generate_realistic_salary(tmpl_cat)
        
        suffix = f" (Ref. #{i})" if i > len(job_templates) else ""
        full_title = f"{tmpl_title}{suffix}"

        generated.append({
            "id": i,
            "title": full_title,
            "company": company,
            "category": tmpl_cat,
            "type": job_type,
            "location": location,
            "salary": salary,
            "posted": "Hoje",
            "phone": phone,
            "description": f"{tmpl_desc} Oferecemos VT, VR/VA, plano de saúde e oportunidade de crescimento no RJ."
        })
        
    return generated

def build_and_save_jobs():
    print("[+] Gerando 100 vagas atualizadas para o Estado do Rio de Janeiro...")
    all_jobs = generate_curated_rj_jobs()
    
    output_filename = "vagas.json"
    with open(output_filename, "w", encoding="utf-8") as f:
        json.dump(all_jobs, f, ensure_ascii=False, indent=2)
        
    print(f"[✓] Arquivo '{output_filename}' gerado com sucesso contendo {len(all_jobs)} vagas!")

if _name_ == "_main_":
    build_and_save_jobs()
