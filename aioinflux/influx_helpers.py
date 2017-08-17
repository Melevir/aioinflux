from datetime import datetime

import aiohttp
import async_timeout


async def safe_send_metric_to_influx_general(measurement_name, value, influx_host, influx_port, influx_db, influx_login, influx_password, exception_callback):
    try:
        await send_metric_to_influx(
            measurement_name,
            value,
            influx_host=influx_host,
            influx_port=influx_port,
            influx_db=influx_db,
            influx_login=influx_login,
            influx_password=influx_password,
        )
    except Exception as e:
        exception_callback(e)


async def send_metric_to_influx(measurement_name, value, influx_host='http://localhost', influx_port=8086, influx_db='test', influx_login=None, influx_password=None):
    write_url = '%s:%s/write' % (influx_host, influx_port)
    timestamp_to_send = int(datetime.now().timestamp() * 1000000000)
    data_to_send = '%s value=%s %s' % (measurement_name, value, timestamp_to_send)
    async with aiohttp.ClientSession() as session:
        await make_post_request(
            session,
            write_url,
            data_to_send,
            params={'db': influx_db},
            basic_auth_login=influx_login,
            basic_auth_password=influx_password
        )


async def make_post_request(session, url, data, params=None, basic_auth_login=None, basic_auth_password=None, timeout_sec=1):
    if basic_auth_login is not None and basic_auth_password is not None:
        auth = aiohttp.BasicAuth(basic_auth_login, basic_auth_password)
    else:
        auth = None
    with async_timeout.timeout(timeout_sec):
        async with session.post(url, data=data, params=params, auth=auth) as response:
            return await response.text()
