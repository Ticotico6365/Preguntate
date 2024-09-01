import random
from datetime import datetime

# Se repite la primera pregunta

from PreguntasApp.models import Pregunta

preguntas = []
preguntas_respondiodias = []

def empezar(bbdd_preguntas):
    if len(preguntas_respondiodias) > 0:
        reiniciar()

    # Para meter preguntas de prueba en la base de datos
    if Pregunta.objects.all().count() == 0:
        meter_preguntas()
        bbdd_preguntas = Pregunta.objects.all().values_list('pregunta_text', flat=True)

        return empezar(bbdd_preguntas)

    for pregunta in bbdd_preguntas:
        preguntas.append(pregunta)
    random.shuffle(preguntas)

def extraer_pregunta():
    if len(preguntas) == 0:
        empezar(preguntas)
    pregunta = preguntas.pop()
    preguntas_respondiodias.append(pregunta)
    return pregunta

def reiniciar():
    preguntas.clear()
    preguntas_respondiodias.clear()


def meter_preguntas():
    preguntas = [
        '¿Cuáles son tus Red Flags a la hora de salir amorosamente con alguien?',
        'Menciona algo que las personas de tu sexo opuesto sepan hacer muy bien.',
        'Menciona algo que las personas de tu sexo opuesto no sepan hacer nada bien.',
        '¿Cuánto tiempo sueles pasar solo?', '¿Pierdes interés cuando un chico/a te ama demasiado?',
        '¿Qué indirectas le haces al / a la que te gusta?', '¿Dónde has metido la polla en este último mes?',
        '¿Qué es lo que menos te gusta de ti cuando te enamoras?',
        '¿Quién va primero el/la novio/a o los mejores amigos?', 'Di una frase de tu película favorita.',
        '¿Por qué podrías ir a la cárcel?', '¿Por qué podrías ir a la cárcel? Que respondan tus amigos.',
        '¿Cuál es la canción que te hace sentir en paz?', '¿Quieres dejar de ocultar algo?',
        '¿Cuál es el video más largo que te has visto?', '¿Cuál es la peli que más te recuerda a tus padres?',
        '¿Qué cultura te gusta más la oriental o la occidental?', 'Tienes cascos alámbricos o inalámbricos.',
        '¿Cuál es tu prenda favorita?', '¿Cuánto tiempo puede estar el agua de tu cuarto encima de tu mesa?',
        '¿Qué cosas te estás perdiendo de la vida?', 'Di 3 cosas por las que merece la pena vivir.',
        '¿Cuál es el jefe de videojuego que más te ha costado matar?', '¿Cómo es tu cartera?',
        '¿Cuál es el mejor juego para jugar en clase?', '¿De qué tendría que haber una aplicación?',
        '¿Qué preguntarías al rey?', '¿Cuál es el mejor rey?', '¿Cuál es el mejor rey de tu país?',
        'Di 5 razones por las que se debería o no tener novio/a.', '¿Te gusta la poesía?',
        '¿Cuál es tu canción de amor?', '¿Alguna vez alguien te ha dedicado una playlist?',
        '¿Qué canción no puedes poner en ningún lado, pero te encanta?', '¿Qué es una persona sin emociones?',
        '¿Quién es superior a ti?', 'Estas en una boda, arruínala en 3 palabras.',
        '¿A qué lugar irías si fueras invisible?', '¿Qué es lo más intocable de tu teléfono?',
        '¿Qué es lo malo del odio?',
        'Cuando estas durmiendo en casa de tu amigo ¿De qué eres? De despertarte antes que tu amigo, de levantarte a la vez o de despertar después.',
        '¿Cuál es el meme que siempre te hace reír?', '¿Dejas que tu mente tome el control de tus sentimientos?',
        '¿Qué es lo más bizarro que se te ha pasado por la cabeza?',
        '¿Qué cosa estás postergando que es importante para ti? ¿Por qué lo haces?',
        'Si estuvieras en un lugar con todas las cosas que has perdido ¿Qué sería lo primero que buscarías?',
        'Si estuvieras en un lugar con todos los amigos que has perdido ¿A quién buscarías primero?',
        '¿Qué pasaría si con solo pensar un deseo se cumple?',
        '¿Sabes que hay personas que de verdad se preocupan por ti?', '¿Cuál es tu dejar en visto más largo?',
        '¿Cuál es tu terapia cuando estas mal?', '¿Con quién eres más competitivo?', '¿Tuviste buena infancia?',
        'Di 5 canciones que te cambiaron la vida', '¿Qué canción no puedes escuchar?',
        '¿Qué canciones enseñarías a tus nietos?', '¿A quién te pillarías?', '¿Qué canción enseñarías a tus hijos?',
        '¿Cuánto te mide la polla?', '¿Cuál es tu álbum musical favorito?',
        '¿Cuál es el estado de ánimo más desagradable?', '¿Te gustan las pegatinas?',
        '¿Cuáles son tus bienaventuranzas?', '¿Qué opinas de la frase Todos/as son iguales?',
        'Si pudieras ser un personaje de dibujos animados. ¿Quién serías y por qué?',
        '¿Cómo te gustaría decorar tu cuarto?', '¿Tienes pito?', '¿Cuál es tu opinión sobre legalizar la prostitución?',
        '¿Qué es lo que más valoras de la amistad?', '¿Un piquito?',
        '¿Los números pares y naturales son más que los números naturales?',
        '¿Qué es lo más absurdo que guardas? ¿Por qué?', 'Unicoos o Susiprofe', '¿Qué necesitas para estar feliz?',
        '¿Cómo crees que la globalización ha afectado a la cultura?', '¿Cuál es la cosa más rara que te ha pasado?',
        '¿Qué opinas de la libertad de expresión?', '¿Quién ganaría en un torneo de piedra, papel o tijeras?',
        '¿Te gusta la ópera?', '¿A qué comunidad muerta perteneces?', '¿Qué juego es nada sin mods?',
        '¿Cuál ha sido el mejor momento de tu vida?', '¿Verías ético clonar dinosaurios?',
        'Di una serie para hacer un maratón', 'Di una canción que te haga llorar', '¿Te drogas?',
        'Educación tradicional o educación en línea', '¿Crees que está aumentando el sexo entre menores?',
        'Califica del 1 al 10 a la persona de tu derecha', '¿Cuál es la despedida más triste que has tenido?',
        '¿Cómo te han ido las notas?', '¿Si ser delito fuera un disléxico? ¿Lo serías?', '¿Estás hot?',
        '¿Dónde te gusta guardar tus cosas?', '¿Qué piensas que es lo más importante de una relación de amistad?',
        '¿Cuál es tu perspectiva sobre la inteligencia artificial en la toma de decisiones éticas?',
        '¿Qué es lo más absurdo que has hecho?', '¿Cuál es el peor hábito que tienes?',
        '¿Te la han chupado alguna vez?', 'Piscina o playa',
        '¿Te gustaría que una inteligencia extraterrestre suficientemente avanzada como para contactar con nosotros contacte con nosotros?',
        '¿Cómo te gustaría bailar con un/a chico/a?', '¿Cuál es el videojuego que más te ha marcado?',
        '¿A quién le tienes que dar las gracias por algo? Si está presente te invito a que se las des.',
        '¿Cómo te va la vida?', '¿Te gusta dibujar?', '¿Qué es la cosa más antigua que conservas?',
        '¿Cuál es la mejor comida? El desayuno, media mañana, la comida, la merienda, la cena o comerse el frigorífico a las 3am.',
        '¿Tu historial de youtube está limpio o sucio?', '¿Cuál es tu opinión sobre el feminismo?',
        '¿Qué opinas de que yo solo sé que no sé nada?', '¿Crees que las redes sociales están mal reguladas?',
        '¿Cuál ha sido el mejor día con los panas?', '¿Cuál es peor el baño de los hombres o el de las mujeres?',
        '¿Qué deporte te gustaría que existiese?', '¿A quién le darías tu muñeco vudú?',
        '¿Te identificas con alguna canción?', '¿Qué opinas de las personas que hablan demasiado de lo que saben?',
        '¿Qué juego juegas últimamente?', '¿Si pudieras ser famoso por algo, de que te gustaría destacar?',
        'Haz una tierlist de las comunidades autónomas', '¿Cuál ha sido la película con la mayor traición?',
        '¿Crees en los extraterrestres?', '¿Por qué os gustan los dildos?', '¿Cuál es tu coche favorito?',
        '¿Me tienes que contar alguna cosa importante que no sepa o que esté en duda?',
        'Di una canción para declararte al amor de tu vida.', '¿Cuántas cosas llevas en la cartera?',
        'El conjunto formado por todos los conjuntos que no son miembros de sí mismos. ¿Es acaso miembro de sí mismo?',
        '¿Cuál ha sido la serie más cursi que has visto?',
        '¿Crees que debería de haber restricciones en el acceso a las redes sociales?',
        '¿Cuál es la serie más dramática que has visto?', '¿Qué es lo que más orgullo te da?',
        '¿Cuál ha sido la gestión más problemática que has hecho?', '¿Qué amigo hace tiempo que no ves?',
        '¿Cuál es el juego con más perros jugando?', '¿A qué hora te sueles acostar?',
        '¿Te gusta pescar en los videojuegos?', '¿Qué es un amigo?',
        '¿Cómo crees que la religión afecta a nuestras vidas?', 'Di 5 canciones para el fin del mundo',
        '¿Qué pasaría si se desvelasen las ideas políticas de tu grupo de amigos?',
        '¿Qué es lo más interesante que te has apostado a piedra papel o tijeras?', '¿Cuánto pesas?',
        '¿Piensas con frecuencia cómo te sientes?', '¿Crees que las redes sociales solapan la información?',
        'Prefieres enviar mensajes de texto o audios', 'Si te pudieras cambiar el nombre ¿Cuál elegirías?',
        '¿Cuál es la cosa más cara que has comprado sin necesidad?',
        '¿La tortilla tiene o no tiene que llevar cebolla?', '¿Qué opinas de tus años en el colegio?',
        'Di una canción de tu banda favorita.', '¿Cuál es el villano que tiene derecho a ser malo?',
        '¿Qué libro te ha dejado una gran impresión de la vida?',
        'Comodín: Hazle una pregunta a alguien. Las tiene que responder si o si, si no colleja nivel medio.',
        '¿Quién es más poderoso Shrek o Gru?', '¿Confías en cada persona aquí presentes?',
        'Di una frase que te haya marcado, y si puedes de donde la has sacado.',
        '¿Qué se sentiría que quien te prometió amarte toda la vida ahora está en los brazos de otro diciéndole lo mismo?',
        '¿Cómo son las explicaciones de tus profesores?', 'Si dominaras el mundo. ¿Qué harías?',
        '¿Qué comida no te cansarías de comer?', '¿Quién te ha influenciado más en esta vida?',
        '¿Qué haces cuando estás depre?', '¿Qué significa esto HDPLMQTP?', '¿Cuál es el mejor chiste que conoces?',
        '¿Cómo tienes tu goma de borrar?', '¿Cuál es tu comida favorita?', '¿Qué es lo que más te pone?',
        '¿Cómo te sentirías si pillas a tu pareja dándose autoplacer?', '¿Quién es lo/la que más te pone?',
        '¿Qué es lo que más bonito que te han dedicado?', '¿Cuál ha sido la serie con la mayor traición?',
        '¿Cuál es el villano más guapo?', 'Cuéntame una historia interesante', '¿Mamada o que te la mamen?',
        '¿Con quién pasas más tiempo?', '¿Tienes sueño?', 'Top 5 videojuegos que has jugado recientemente',
        '¿Qué objeto te llevas a la cama?', '¿Qué representa mejor a tu sexo opuesto?',
        '¿Cuál es la verdad más importante que has aprendido?', '¿Qué es lo último que has comido?',
        '¿Quién es la persona más madura de las presentes?', '¿Qué opinas de la política actual?',
        '¿Cuál es el propósito de la vida, en tu opinión?', '¿Cuál ha sido el consejo ignorado más reciente?',
        '¿Qué tipo de persona eres cuando graban un video para Instagram?', '¿Cuál es tu mejor dibujo?',
        '¿Cómo reaccionarías si tu mejor amigo/a te mande fototeta o fotopito?', 'Coche o moto',
        '¿Cuál es el/ la que te parece más guapo de tu curso?', '¿Qué temes?',
        '¿A quién salvarías en un apocalipsis? ¿Y qué harías con él?', '¿De qué te arrepientes más?', 'Playa o montaña',
        '¿Qué te gusta del fin de semana?', '¿Te tatuarías?', '¿Tú le harías daño a una mujer?', '¿Ere gey?',
        '¿Qué tienes y no usas?', '¿Cada cuánto tiempo piensas en el imperio romano?', '¿Eres de preguntar mucho?',
        '¿Cuándo te diste cuenta que toda tu vida ha pasado en 1 segundo?', '¿En tu familia hay alguna tradición rara?',
        '¿El universo puede desaparecer ya?', '¿Crees que deberíamos tener un gobierno mundial?',
        '¿Crees que puedo matarte aquí y ahora?', '¿Cómo ha evolucionado la cultura en estos años?',
        '¿Cuál es el mejor queso que has probado?', '¿Cuál es tu almohada favorita?', '¿En qué quieres trabajar?',
        '¿A donde te gustaría ir, al pasado o al futuro?', '¿Cuál es la importante de tu vida?',
        'Si despertaras en el último juego que jugaste, cuál sería y cómo de jodido estaría sobrevivir',
        '¿Cuál es el nombre más feo?', 'Califica del 1 al 10 tu móvil',
        '¿Te preocupa algo? (no tienes por qué decirlo)', '¿Podemos vivir en un sueño?',
        '¿Qué es lo que más te gusta hacer en tu tiempo libre?', '¿Cuál es tu juego de mesa favorito?',
        '¿Qué has robado?', '¿Qué te define como persona?', '¿Crees que las personas pueden cambiar?',
        '¿Cuántos enchufes tienes en tu cuarto?', '¿Eres boquerón?', '¿Crees que todo sucede por alguna razón?',
        '¿Qué te hace distinto a los demás?', '¿Qué opinas de la educación sexual como asignatura?',
        'Define tu gusto musical con 3 artistas.', '¿España es o no un imperio?',
        '¿Cómo manejas el estrés y la presión en tu vida diaria?', 'Si fueras un producto. ¿Cuál sería tu eslogan?',
        '¿Qué talento artístico te gustaría tener?', '¿Quién ganaría en un pulso?',
        '¿Cuál es tu especialidad en minecraft?', 'Di 5 canales de youtube interesantes.',
        '¿Cuál es el puzle más complicado que has hecho?', '¿Tienes un artista favorito?',
        '¿Cuál es el video más raro de tu galería?', '¿Cuál es tu juego de móvil favorito?',
        '¿Cuál es tu programa televisivo favorito?', '¿Cómo dé a menudo bebes agua?',
        '¿Cuál es el juego con mejores diálogos?', '¿A dónde irías si pudieras teletransportarte?',
        '¿Qué animal serías por un día?', '¿Qué cambios te gustaría ver en el mundo?',
        '¿Quién es el más guapo/a de los presentes?', '¿Qué es lo que no quieres que te pase?',
        '¿Qué etapa de tu vida no quieres que se repita? ¿Por qué?', '¿Qué enfermedad no querrías tener?',
        'IPhone o Android', '¿Cuál es tu pasatiempo favorito? ¿Cómo empezaste a interesarte en él?',
        '¿Algún bulo que te hayas creído? ¿Cuál? ', '¿Estás contento con tu vida actualmente?',
        '¿Cuál es tu zona favorita en tu casa? ¿Por qué?', 'De los presentes. ¿Quién tiene los mejores abdominales?',
        '¿Qué opinas de las relaciones en secreto?', '¿Qué es más importante ser amado o respetado?',
        'Del 1 al 10 cómo te presionan las personas en los estudios, y cuántas te ayudan y cuántas no.',
        '¿Algún problema físico, como miopía, pies planos, etc.?',
        '¿Qué es lo más raro que has encontrado en ticktock?', '¿Qué es lo peor de la primaria?',
        '¿Tienes ganas de viernes?', '¿Qué torneo verías?', '¿Tienes papelera en tu cuarto?',
        '¿Qué opinas de las personas que usan tirantes?', '¿Escuchas la radio?',
        '¿Crees que la tecnología nos deshumaniza?', '¿Alguna vez te has hecho un test de personalidad? ¿Qué salió?',
        '¿Cuál es el sitio más raro donde has dormido?', '¿Cuál es el juego que la comunidad ha hecho mejores cosas?',
        '¿Te gusta que te rasquen la espalda?', '¿Alguna vez te han dedicado una canción?',
        '¿Cuál es tu embutido favorito?', '¿Cómo te gustaría morir?',
        '¿Cuál es la película que más lagunas tiene y que hayas visto?', 'Serme sincero y dime. ¿Estás bien?',
        '¿De qué olor harías una colonia?', '¿Te gusta tu spawn?', '¿Cuál es la moda que más has seguido?',
        '¿Cuál es el regalo más absurdo que guardas con cariño? ¿Quién te lo dio?',
        '¿Ves el almacenaje de residuos radiactivos como una solución para deshacernos de estos residuos?',
        '¿Necesitas ayuda?', '¿Cuál es la relación entre la felicidad y el sentido de la vida?',
        '¿Cuál es el mejor youtuber o streamer que hay?', '¿Qué tipo de películas te gustan?', '¿Qué te apasiona?',
        '¿Qué harías si tu foto de perfil existiera y te visitara?', '¿Qué opinas de la adopción?',
        '¿Qué es lo mejor de la primaria?', 'Di tu orientación sexual', '¿Qué libro te cambió la vida?',
        '¿Qué es lo que más ansias y tienes a la vista?', 'Hamburguesa o pizza',
        '¿Cuenta tu historia de cómo, por qué y a quién, para llegar aquí?',
        '¿Cuál es la mejor persona que has conocido este año?', '¿Quién te escribe más?',
        '¿Cuál es el personaje con mejor culo?', '¿Cuál ha sido la mayor lección que has aprendido hasta ahora?',
        '¿Dejarías que una IA gobernase un país?', '¿Te han traicionado?', '¿Haces huelga? ¿Cuándo es la próxima?',
        '¿Qué opinas del cinismo?', '¿Cuál es tu juego de mesa favorito?', '¿Qué se necesita para impresionarte?',
        '¿Cuál ha sido la escena de serie/película que más coraje te ha dado?',
        '¿Cuál es tu película favorita cuando estás enfermo?',
        '¿Cuál es el recuerdo más significativo que tienes con tus amigos?',
        '¿Cuál es el deporte más raro que has visto?', '¿Te gustaría un preguntas random H2O?',
        '¿Cuál es tu músico favorito?', '¿La iglesia hace bien?', '¿Cuál es la mejor película de coches?',
        'Culo o tetas / gorda o larga', '¿Has probado la autofelación? ¿Te gustaría?', 'Arriba o abajo en la cama',
        '¿Cuál es la foto más rara de tu galería?', '¿Cuál es el objeto más extraño que hay en tu casa?',
        '¿Cuál es el amigo que más te ha ayudado? (puede haber más de uno)', '¿Crees que hay una cultura global?',
        '¿Te gusta la purpurina?', '¿Cómo te sientes?', 'Di una canción que te pone hot', '¿Qué te hace reír siempre?',
        '¿Cuántas preguntas tiene el juego?', '¿Con quién hablas más?', '¿Sabes lo que significa inferir?',
        '¿Cuál es tu foto más mítica?', '¿Alguna vez te has cabreado con alguno de los presentes?',
        '¿Cuáles son tus hobbies?', 'Si no fueras tú. ¿Qué serías?',
        '¿Qué características tiene una pareja que las diferencia?', '¿Eres un acosador sexual?',
        '¿Cuál es la canción más soez que escuchas?', '¿Qué canción que no entiende nadie escuchas?',
        '¿Dónde te gustaría hacerlo?', '¿Cómo dé a menudo piensas en Goku?',
        '¿Cuál es la persona aquí presente en la que más piensas?', '¿Crees que la tecnología nos ha hecho perezosos?',
        '¿Cuál fue tu juguete favorito de la infancia?', '¿Qué legado te gustaría dejar en el mundo?',
        '¿Qué te gustaría hacer si tuvieras más tiempo libre?', '¿Cuál es tu caramelo favorito?',
        'Minecraft o terraria', '¿Cuál es la importancia de la filosofía?', '¿Qué es lo que más te gusta de tu vida?',
        '¿Qué es lo que no entiendes?', 'Ser inmortal o vivir 100 años de vida', '¿Cómo llamarías a tu isla?',
        '¿Si pudieras tener cualquier coche cual elegirías?', '¿Eres un moñas?',
        '¿Cuál es la/el más culón/na del curso?', '¿Cuál es tu BSO de videojuego favorita?',
        '¿Qué video de youtube llevas en el corazón?', '¿Cuál es el sitio donde peor huele?',
        '¿Qué representa mejor a una mujer?', '¿Qué representa mejor a un hombre?',
        'Explica tu autodefinición. ¿Cómo has llegado hasta aquí?', '¿Qué es lo más inútil que has hecho?',
        '¿Cuál sería tu realidad alternativa favorita?', '¿Cuál es el puzle más complicado que has hecho en un juego?',
        '¿Odias, pero respetas?', '¿Te gustaría ser mago?', '¿Cuál es la profesión más peligrosa?',
        'En 24h se acaba el mundo y todo el mundo lo sabe. ¿Qué harías?',
        '¿Cuál es la cosa más absurda que te han regalado?', '¿Querrías ir al espacio?',
        'Del 1 al 10. ¿Qué opinas de las faldas?', 'Dime 4 series buenas',
        'Di 5 maneras de decir “me da igual” cada uno y sin que se repita',
        '¿Cuál es la película más corta que te has visto?', 'Del 1 al 10 cómo es tu contacto masculino y femenino',
        '¿Te dan miedo las mujeres?', '¿A quién resucitarías?', '¿Con quién discutes más?',
        '¿Qué pasaría si pudieras leer la mente de las personas?', '¿Cuál es la apuesta más rara que has hecho?',
        '¿He harías si todo fuera legal durante 8h?', '¿Cuál es el amigo que más te ha marcado?',
        '¿Qué opinas del amor? ¿Qué es lo más importante para ti en una relación romántica?', '¿Heres un heterobásico?',
        '¿Sabes algo que no aparece en Wikipedia?',
        '¿Cuál es tu opinión sobre las relaciones interpersonales y cómo podríamos mejorarlas?',
        'De todas las personas que están al alcance de tu vista. ¿Con quién te gustaría salir más?',
        '¿Cuál es tu moda favorita?', 'Top 5 coches clásicos', '¿Qué has hecho esta semana?',
        '¿Con cuál juego dices cosas malpensables?', '¿Quién es tu némesis y en qué lo es?',
        '¿Cuál es la cosa más épicamente imposible que te ha pasado?', 'Cuenta la mayor borrachera que has tenido',
        '¿Qué te gustaría tener con tus límites económicos?', '¿Cuál es tu zumo favorito?',
        '¿De qué color son tus boxers?', '¿Qué animal representa mejor tu personalidad?', '¿Cuál es tu baile favorito?',
        '¿Cuál es tu opinión sobre la política actual?', '¿Alguna vez te has dado pena a ti mismo?',
        'Sitio más raro donde te has liado/ hecho una paja o dedo', '¿De qué año es tu móvil?',
        'De lo que estás haciendo (estudios o trabajo). ¿Qué es lo que mejor se te da?',
        '¿De qué te gustaría abrir un servidor con los colegas?', '¿Te gusta preguntar?',
        '¿Cómo de importante es tener una cultura general antes que saber otras disciplinas como inglés?',
        '¿Crees que la sociedad se respeta?', '¿Os respetáis entre tus amigos?',
        '¿Qué es lo que más usas y más te dura?', '¿En qué juego has muerto más veces?',
        '¿A quién matarías de tu instituto?', '¿Hacen falta las normas?',
        '¿Cuál es la broma más pesada que te han hecho?', '¿Qué música te pones para jugar?'
    ]

    for pregunta in preguntas:
        new = Pregunta()
        new.pregunta_text = pregunta
        new.pub_date = datetime.now()
        new.user_id = 1
        posibilidades = [True, False]
        new.is_private = random.choice(posibilidades)
        if new.is_private:
            new.is_active = False
        else:
            new.is_active = random.choice(posibilidades)
        new.save()

