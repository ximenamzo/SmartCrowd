/*RETURNS TRIGGER AS $$
BEGIN
    NEW.fec_mod = NOW() AT TIME ZONE 'America/Mexico_City';
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER actualizar_modificacion
BEFORE UPDATE ON public."aforoReg_place"
FOR EACH ROW
EXECUTE FUNCTION actualizar_fecha_modificacion();*/


/*UPDATE public."aforoReg_place" SET nomlugar = 'Casa Ximenita' WHERE id = 4;*/


/*INSERT INTO public."aforoReg_camera" (id_place, lugarcam, num_cam_lug) VALUES (8, 'Laptop Ximena', 1);*/
