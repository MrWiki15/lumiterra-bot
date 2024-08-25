import datetime

async def on_command_error(error, info):
    try:
        with open('../logs/logs_errors.txt', 'a') as f:
            f.write(
                "................................................................................................................................................\n"
            )
            f.write(
                "................................................................................................................................................\n"
            )
            f.write(f"""Se detecto un error en el comando: /{info.command.name}.\n\n 
                        Desde el servidor : {info.guild.name} de id = {info.guild.id}
                        Desde el canal : #{info.channel.name}# de id = {info.channel.id}
                        Desde el usuario : @{info.user.name}@ de id = {info.user.id}
                        A la hora: {datetime.now()}""")
            f.write(
                "................................................................................................................................................\n"
            ) 
            f.write(f"Error: {str(error)}\n")
            f.write(
                "................................................................................................................................................\n"
            )
    except Exception as e:
        print(f"Ocurrio un error al escribir el error en el log: {str(e)}")