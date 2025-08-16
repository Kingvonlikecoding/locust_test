| 概念          | 说明                                  |
| ----------- | ----------------------------------- |
| **User**    | 模拟的虚拟用户，每个用户会按你写的 Python 脚本执行任务。    |
| **Task**    | 用户执行的具体操作（比如发一个 HTTP 请求）。           |
| **Weight**  | 控制不同任务的执行频率（比如登录任务权重高，浏览任务权重低）。     |
| **Hatch**   | 每秒启动多少用户（类似 JMeter 的线程组里的 Ramp-Up）。 |
| **Metrics** | 自动收集的指标：RPS（每秒请求数）、响应时间、失败率等。       |

cm:
locust -f locustfile.py
-f 参数是 --locustfile 的缩写，用于指定要运行的Locust测试文件路径

locust -f locustfile.py --headless -u 100 -r 10 -t 60s --html report.html
- -u 100 ：设置并发用户数（ users ），模拟100个同时在线的用户。
- -r 10 ：设置用户生成速率（ spawn rate ），每秒新增10个用户，直到达到 -u 设置的100个用户
- -t 60s ：设置测试持续时间（ time ），这里为60秒