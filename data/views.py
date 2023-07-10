from django.shortcuts import render
import json
import pymysql

# Create your views here.

def predict(request):
    # MySQL 데이터베이스 연결
    conn = pymysql.connect(host='m2-rds.cm53ld3fibe2.ap-northeast-1.rds.amazonaws.com', port=3306, user='adminm2', passwd='adminm211335588', db='farm_db', charset='utf8')
    cur = conn.cursor()

    # 쿼리 실행
    query =  "SELECT * FROM enviroment_day ORDER BY DAT ASC LIMIT 5;"
    cur.execute(query)
    rows = cur.fetchall()

    # 결과 처리 : 시간별 내부온도 관측치
    main_line_lbl = []
    main_line_val = []

    for row in rows:
        main_line_lbl.append(row[0])
        main_line_val.append(row[1])
    # 연결 및 커서 닫기
    cur.close()
    conn.close()

    # 결과를 JSON 형식으로 변환
    contx_dic = {
        'main_line_lbl': main_line_lbl,
        'main_line_val': main_line_val,
    }
    result = json.dumps(contx_dic, ensure_ascii=False)
    print(result)
    context = {'result': result,'rows':rows}

    return render(request, 'data/predict.html', context)


def graph(request):    # MySQL 데이터베이스 연결
    conn = pymysql.connect(host='m2-rds.cm53ld3fibe2.ap-northeast-1.rds.amazonaws.com', port=3306, user='adminm2', passwd='adminm211335588', db='farm_db', charset='utf8')
    cur = conn.cursor()

    # 쿼리 실행
    query =  "SELECT * FROM environment ORDER BY DAT ASC LIMIT 5;"
    cur.execute(query)
    rows = cur.fetchall()
    
    # 결과 처리 : 시간별 내부온도 관측치
    main_line_lbl = []
    main_line_val = []
    for row in rows:
        main_line_lbl.append(row[0])
        main_line_val.append(row[1])

    # 결과 처리 : 시간별 내부습도 관측치
    main_line_lbl2 = []
    main_line_val2 = []
    for row in rows:
        main_line_lbl2.append(row[0])
        main_line_val2.append(row[2])

     # 결과 처리 : 시간별 분무량
    main_line_lbl3 = []
    main_line_val3 = []
    for row in rows:
        main_line_lbl3.append(row[0])
        main_line_val3.append(row[4])
     # 결과 처리 : 시간별 총광량    
    main_line_lbl4 = []
    main_line_val4 = []
    for row in rows:
        main_line_lbl4.append(row[0])
        main_line_val4.append(row[6])

    # 연결 및 커서 닫기
    cur.close()
    conn.close()

    # 결과를 JSON 형식으로 변환
    contx_dic = {
        'main_line_lbl': main_line_lbl,
        'main_line_val': main_line_val,
                'main_line_lbl2': main_line_lbl2,
        'main_line_val2': main_line_val2,
                'main_line_lbl3': main_line_lbl3,
        'main_line_val3': main_line_val3,
                'main_line_lbl4': main_line_lbl4,
        'main_line_val4': main_line_val4,

    }
    result = json.dumps(contx_dic, ensure_ascii=False)
    print(result)
    context = {'result': result,'rows':rows}
    return render(request, 'data/graph.html', context)



