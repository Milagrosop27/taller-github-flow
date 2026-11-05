TASA_IMPUEST0 = {"CO": 0.19, "MX": 0.16, "CL": 0.19, "AR": 0.21, "PE": 0.18}


def procesar_pago_usuario(usuario, tarjeta, monto, pais, es_vip):
    if not usuario or not usuario.get('activo'):
        print("Usuario inactivo o inválido.")
        return False

    if tarjeta.get('saldo', 0) < monto:
        print("Saldo insuficiente en la tarjeta.")
        return False

    monto_final = monto
    if es_vip and monto > 1000:
        monto_final *= 0.80
    elif es_vip:
        monto_final *= 0.90

    impuesto = TASA_IMPUEST0.get(pais, 0.0)
    monto_final += monto_final * impuesto

    tarjeta['saldo'] = monto_final
    return True
