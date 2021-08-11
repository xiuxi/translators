# coding=utf-8
# author=UlionTse

import loguru
from translators.apis import *


query_text1 = '季姬寂，集鸡，鸡即棘鸡。棘鸡饥叽，季姬及箕稷济鸡。👍👍👍'
query_text2 = """北国风光，千里冰封，万里雪飘。望长城内外，惟余莽莽；大河上下，顿失滔滔。山舞银蛇，原驰蜡象，欲与天公试比高。\n
须晴日，看红装素裹，分外妖娆。江山如此多娇，引无数英雄竞折腰。惜秦皇汉武，略输文采；唐宗宋祖，稍逊风骚。一代天骄，成吉思汗，只识弯弓射大雕。\n
俱往矣，数风流人物，还看今朝。\n
"""
query_text3 = 'All the past, a number of heroes, but also look at the present.'


html_text = """
<!DOCTYPE html>
<html>
<body>

<address>
Written by <a href="mailto:webmaster@example.com">Donald Duck</a>.<br> 
Visit us at:<br>
Example.com<br>
Box 564, Disneyland<br>
USA
</address>

<p>
北国风光，千里冰封，万里雪飘。望长城内外，惟余莽莽；大河上下，顿失滔滔。山舞银蛇，原驰蜡象，欲与天公试比高。\n
须晴日，看红装素裹，分外妖娆。江山如此多娇，引无数英雄竞折腰。惜秦皇汉武，略输文采；唐宗宋祖，稍逊风骚。一代天骄，成吉思汗，只识弯弓射大雕。\n
俱往矣，数风流人物，还看今朝。\n
</p>

<p></p>
<p> </p>
<p>5%</p>
<p>123\t</p>

<strong>hello world</strong>

<div class="codetext notranslate">
<code>
import translators as ts
</code>
</div>

</body>
</html>
"""

@Tse.time_stat
@loguru.logger.catch
def test0():
    r = translate_html(html_text, to_language='zh', translator=google)
    print(r)


@loguru.logger.catch
def test1():
    for query_text in [query_text1, query_text2, query_text3]:
        print(alibaba(query_text))
        print(baidu(query_text))
        print(bing(query_text))
        print(deepl(query_text))
        print(google(query_text))
        print(sogou(query_text))
        print(tencent(query_text))
        print(yandex(query_text))
        print(youdao(query_text))


if __name__ == "__main__":
    test0()
    test1()
