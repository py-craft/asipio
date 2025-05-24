import argparse
import asyncio
import logging

import aiovoip

sip_config = {
    'srv_host': 'xxxxxx',
    'srv_port': '7000',
    'realm': 'XXXXXX',
    'user': 'YYYYYY',
    'pwd': 'ZZZZZZ',
    'local_ip': '127.0.0.1',
    'local_port': 6000
}


async def on_invite(request, message):
    print('Call ringing!')
    # Sending 100 Trying
    dialog = await request.prepare(status_code=100)
    # Sending 180 Ringing
    await dialog.reply(message, status_code=180)
    print('Ringing for 3 seconds!')
    await asyncio.sleep(3)
    # Sending 200 OK - answer the call
    await dialog.reply(message, status_code=200)
    print('Call started!')

    async for message in dialog:
        await dialog.reply(message, 200)
        if message.method == 'BYE':
            print("Call ended!")
            break

class Dialplan(aiovoip.BaseDialplan):

    async def resolve(self, *args, **kwargs):
        await super().resolve(*args, **kwargs)

        if kwargs['method'] == 'INVITE':
            return on_invite


def start(app, protocol):
    app.loop.run_until_complete(
        app.run(
            protocol=protocol,
            local_addr=(sip_config['local_ip'], sip_config['local_port'])))

    print('Serving on {} {}'.format(
        (sip_config['local_ip'], sip_config['local_port']), protocol))

    try:
        app.loop.run_forever()
    except KeyboardInterrupt:
        pass

    print('Closing')
    app.loop.run_until_complete(app.close())


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--protocol', default='udp')
    args = parser.parse_args()

    loop = asyncio.get_event_loop()
    app = aiovoip.Application(loop=loop, dialplan=Dialplan())

    if args.protocol == 'udp':
        start(app, aiovoip.UDP)
    elif args.protocol == 'tcp':
        start(app, aiovoip.TCP)
    elif args.protocol == 'ws':
        start(app, aiovoip.WS)
    else:
        raise RuntimeError("Unsupported protocol: {}".format(args.protocol))

    loop.close()


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    main()
