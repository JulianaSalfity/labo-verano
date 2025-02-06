# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 00:17:09 2025

@author: Adrian
"""


# Importamos bibliotecas
import pandas as pd
import duckdb as dd
print(dd.__version__)

#%%===========================================================================
# Importamos los datasets que vamos a utilizar en este programa
#=============================================================================

carpeta = r'C:/Users/Adrian/Downloads/'

provincia      = pd.read_csv(carpeta+"provincia.csv")
tipoevento    = pd.read_csv(carpeta+"tipoevento.csv")
departamento   = pd.read_csv(carpeta+"departamento.csv")
grupoetario        = pd.read_csv(carpeta+"grupoetario.csv")
casos = pd.read_csv(carpeta+"casos.csv")


#%%===========================================================================
# EJERCICIO 1
#=============================================================================
#%% Ejercicio 1.a
consultaSQL = """
                SELECT descripcion FROM departamento
              """

dataframeResultado = dd.sql(consultaSQL).df()

#%%Ejercicio 1.b
consultaSQL = """
                SELECT DISTINCT descripcion FROM departamento
              """

dataframeResultado = dd.sql(consultaSQL).df()
#%%Ejercicio 1.c
consultaSQL = """
                SELECT id,descripcion FROM departamento
              """

dataframeResultado = dd.sql(consultaSQL).df()
#%%Ejercicio 1.d
consultaSQL = """
                SELECT * FROM departamento
              """

dataframeResultado = dd.sql(consultaSQL).df()
#%%Ejercicio 1.e
consultaSQL = """
                SELECT id AS codigo_depto ,descripcion AS nombre_depto
                FROM departamento
              """

dataframeResultado = dd.sql(consultaSQL).df()
#%%Ejercicio 1.f
consultaSQL = """
                SELECT * FROM departamento
                WHERE id_provincia = 54
              """

dataframeResultado = dd.sql(consultaSQL).df()
#%%Ejercicio 1.g
consultaSQL = """
                SELECT * FROM departamento
                WHERE id_provincia = 22 OR id_provincia = 78 OR id_provincia = 86
              """

dataframeResultado = dd.sql(consultaSQL).df()
#%%Ejercicio 1.h
consultaSQL = """
                SELECT * FROM departamento
                WHERE id_provincia >= 50 AND id_provincia <= 59
              """

dataframeResultado = dd.sql(consultaSQL).df()
#%%===========================================================================
# EJERCICIO 2
#=============================================================================
#%%Ejercicio 2.a
consultaSQL = """
                    SELECT DISTINCT departamento.id, departamento.descripcion, provincia.descripcion AS provincia
                    FROM departamento
                INNER JOIN provincia
                    ON departamento.id_provincia = provincia.id

              """

depto_por_provincia = dd.sql(consultaSQL).df()
#%%Ejercicio 2.c
departamentos_en_chaco = """
                    SELECT DISTINCT departamento.id, provincia.descripcion AS provincia
                    FROM departamento
                INNER JOIN provincia
                    ON departamento.id_provincia = provincia.id
                    WHERE provincia.descripcion = 'Chaco'

              """
departamentos_en_chaco = dd.sql(departamentos_en_chaco).df()

consultaSQL = """
                    SELECT DISTINCT casos.id, casos.id_tipoevento, casos.anio, casos.semana_epidemiologica, casos.id_grupoetario, casos.cantidad 
                    FROM casos
                INNER JOIN departamentos_en_chaco
                    ON casos.id_depto = departamentos_en_chaco.id

              """

dataframeResultado = dd.sql(consultaSQL).df()

#%%Ejercicio 2.d
departamentos_en_provBsAs = """
                    SELECT DISTINCT departamento.id, provincia.descripcion AS provincia
                    FROM departamento
                INNER JOIN provincia
                    ON departamento.id_provincia = provincia.id
                    WHERE provincia.descripcion = 'Buenos Aires'

              """
departamentos_en_provBsAs = dd.sql(departamentos_en_provBsAs).df()

consultaSQL = """
                    SELECT DISTINCT casos.id, casos.id_tipoevento, casos.anio, casos.semana_epidemiologica, casos.id_grupoetario, casos.cantidad 
                    FROM casos
                INNER JOIN departamentos_en_provBsAs
                    ON casos.id_depto = departamentos_en_provBsAs.id
                    AND casos.cantidad > 10

              """

dataframeResultado = dd.sql(consultaSQL).df()

#%%===========================================================================
# EJERCICIO 3
#=============================================================================
#%%Ejercicio 3.a
consultaSQL = """
                        SELECT DISTINCT descripcion
                        FROM departamento AS d
                    LEFT OUTER JOIN casos AS c
                    ON d.id != c.id_depto
            
                    
              """

dataframeResultado = dd.sql(consultaSQL).df()

#%%Ejercicio 3.b

#%%===========================================================================
# EJERCICIO 4
#=============================================================================
#%%Ejercicio 4.a

consultaSQL = """
                SELECT SUM(cantidad) AS cantidadCasos
                FROM casos

              """

dataframeResultado = dd.sql(consultaSQL).df()


#%%Ejercicio 4.b

casos_con_tipos = """
                    SELECT DISTINCT casos.id, casos.id_depto , casos.anio, casos.semana_epidemiologica, casos.id_grupoetario, casos.cantidad, t.descripcion
                    FROM casos
                INNER JOIN tipoevento AS t
                    ON casos.id_tipoevento = t.id
              """
              
#casos.id, casos.id_depto , casos.anio, casos.semana_epidemiologica, casos.id_grupoetario, casos.cantidad, t.descripcion
casos_con_tipos = dd.sql(casos_con_tipos).df()
consultaSQL = """
                SELECT ct.descripcion AS tipo_caso, ct.anio , SUM(ct.cantidad) AS cantidadCasos
                FROM casos_con_tipos AS ct
                GROUP BY tipo_caso, anio
                ORDER BY tipo_caso, anio
              """

dataframeResultado = dd.sql(consultaSQL).df()

#%%Ejercicio 4.c
consultaSQL = """
                SELECT ct.descripcion AS tipo_caso, ct.anio , SUM(ct.cantidad) AS cantidadCasos
                FROM casos_con_tipos AS ct
                WHERE anio = '2020'
                GROUP BY tipo_caso, anio
                ORDER BY tipo_caso, anio
              """

dataframeResultado = dd.sql(consultaSQL).df()
#%%Ejercicio 4.d
consultaSQL = """
                SELECT id_provincia, COUNT(*) AS depto
                FROM departamento
                GROUP BY id_provincia
                ORDER BY id_provincia
              """

dataframeResultado = dd.sql(consultaSQL).df()


#%%Ejercicio 4.e

casos_con_departamentos = """
                    SELECT DISTINCT casos.id, casos.id_tipoevento , casos.anio, casos.semana_epidemiologica, casos.id_grupoetario, casos.cantidad, d.descripcion
                    FROM casos
                INNER JOIN departamento AS d
                    ON casos.id_depto= d.id
              """
              
#casos.id, casos.id_depto , casos.anio, casos.semana_epidemiologica, casos.id_grupoetario, casos.cantidad, t.descripcion
casos_con_departamentos = dd.sql(casos_con_departamentos).df()

total_casos_2019 = """
                    SELECT DISTINCT d.descripcion, SUM(c.cantidad) as cantidad_casos
                    FROM casos AS c
                INNER JOIN departamento AS d
                    ON c.id_depto= d.id
                    GROUP BY d.descripcion
                    """
total_casos_2019 = dd.sql(total_casos_2019).df()


consultaSQL = """
                SELECT descripcion, cantidad_casos
                FROM total_casos_2019 AS tc
                WHERE cantidad_casos =  (MAX(cantidad_casos))
              """

dataframeResultado = dd.sql(consultaSQL).df()


#%%Ejercicio 4.f
consultaSQL = """
                SELECT cd.descripcion AS depto_caso, MIN(cd.cantidad) AS cantidadCasos
                FROM casos_con_departamentos AS cd
                WHERE cd.anio = '2020'
                GROUP BY depto_caso
              """

dataframeResultado = dd.sql(consultaSQL).df()
#%%Ejercicio 4.g


casos_provincia = """
                    SELECT DISTINCT casos.id, casos.id_tipoevento , casos.anio, casos.semana_epidemiologica, casos.id_grupoetario, casos.cantidad, dp.provincia
                    FROM casos
                INNER JOIN depto_por_provincia AS dp
                    ON casos.id_depto= dp.id
                    ORDER BY dp.provincia, casos.anio
              """
casos_provincia = dd.sql(casos_provincia).df()
promedio_casos = """
                    SELECT DISTINCT p.descripcion, c.anio, AVG(c.cantidad) as cantidad_casos
                    FROM casos_provincia AS c
                INNER JOIN provincia AS p
                    ON p.descripcion= c.provincia
                    GROUP BY p.descripcion, c.anio
                    ORDER BY  p.descripcion, c.anio
                    """
promedio_casos = dd.sql(promedio_casos).df()
#%%Ejercicio 4.i


tabla_final = """
                        SELECT DISTINCT provincia, 
                        SUM(cantidad) AS cant_total, 
                        MAX(cantidad) AS cant_max,
                        MIN(cantidad) AS cant_min, 
                        AVG(cantidad) AS cant_promedio
                        FROM casos_provincia
                        WHERE provincia = 'Buenos Aires' AND anio = 2019
                        GROUP BY provincia
                        """

tabla_final = dd.sql(tabla_final).df()

#%%Ejercicio 4.j

tabla_final = """
                        SELECT DISTINCT provincia, 
                        SUM(cantidad) AS cant_total, 
                        MAX(cantidad) AS cant_max,
                        MIN(cantidad) AS cant_min, 
                        AVG(cantidad) AS cant_promedio
                        FROM casos_provincia
                        WHERE provincia = 'Buenos Aires'  AND cantidad > 1000
                        GROUP BY provincia
                        """

tabla_final = dd.sql(tabla_final).df()

#%%Ejercicio 4.k

dn = """
                SELECT DISTINCT cd.descripcion
                FROM casos_con_departamentos AS cd
                WHERE cd.anio = 2019
                GROUP BY cd.descripcion
              """
dv = """
                SELECT DISTINCT cd.descripcion
                FROM casos_con_departamentos AS cd
                WHERE cd.anio = 2020
                GROUP BY cd.descripcion
              """
deptos_prov_2020_2019 = """
                SELECT DISTINCT dn.descripcion AS depto, dp.provincia AS prov
                FROM dn
            INNER JOIN dv
                ON dv.descripcion = dn.descripcion
            INNER JOIN depto_por_provincia AS dp
                ON dp.descripcion = dn.descripcion
                ORDER BY dp.provincia ASC, dn.descripcion DESC
       
                """
promedio_por_depto = """ SELECT DISTINCT descripcion, AVG(cantidad) AS promedio
                        FROM casos_con_departamentos
                        GROUP BY descripcion
                        """
tabla_final = """
                SELECT DISTINCT dp.depto, dp.prov, pd.promedio
                FROM deptos_prov_2020_2019 AS dp
            INNER JOIN promedio_por_depto AS pd
                ON pd.descripcion = dp.depto
                ORDER BY dp.prov ASC, dp.depto DESC
                """
            


dn = dd.sql(dn).df()
dv = dd.sql(dv).df()
deptos_prov_2020_2019 = dd.sql(deptos_prov_2020_2019).df()
promedio_por_depto = dd.sql(promedio_por_depto).df()
tabla_final = dd.sql(tabla_final).df()

#%%Ejercicio 4.l
total_dn = """
                SELECT DISTINCT te.descripcion AS tipo_evento, 
                d.id AS id_depto,
                cd.descripcion AS depto,
                p.id AS id_prov,
                dp.provincia AS prov, 
                SUM(cd.cantidad) AS cant_total
                FROM casos_con_departamentos AS cd
            INNER JOIN tipoevento AS te
                ON te.id = cd.id_tipoevento
            INNER JOIN departamento as d
                ON d.descripcion = cd.descripcion
            INNER JOIN depto_por_provincia AS dp
                ON dp.descripcion = cd.descripcion
            INNER JOIN provincia AS p
                ON dp.provincia = p.descripcion
                WHERE cd.anio = 2019
                GROUP BY cd.descripcion, te.descripcion, d.id, dp.provincia, p.id
              """
total_dv = """
                SELECT DISTINCT 
                d.id AS id_depto,
                SUM(cd.cantidad) AS cant_total
                FROM casos_con_departamentos AS cd
            INNER JOIN departamento as d
                ON d.descripcion = cd.descripcion
                WHERE cd.anio = 2020
                GROUP BY d.id
              """
tabla_final = """
                SELECT DISTINCT tn.tipo_evento, tn.id_depto, tn.depto, tn.id_prov, tn.prov, tn.cant_total AS cant_total2019, tv.cant_total AS cant_total2020
                FROM total_dn AS tn
            INNER JOIN total_dv AS tv
                ON tv.id_depto = tn.id_depto
                ORDER BY tn.prov
                """
total_dn = dd.sql(total_dn).df()
total_dv = dd.sql(total_dv).df()
tabla_final = dd.sql(tabla_final).df()