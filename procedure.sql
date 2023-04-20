/*CREATE OR REPLACE PROCEDURE limpiar_registros() 
LANGUAGE plpgsql
AS $$
BEGIN
    SET TIME ZONE 'America/Mexico_City';
    DELETE FROM public."aforoReg_register" WHERE fecha + hora < now() - interval '24 hours';
END;
$$;*/

/*DROP PROCEDURE IF EXISTS limpiar_tabla();*/

CALL limpiar_registros();

