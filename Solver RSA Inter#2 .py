
from Crypto.Util.number import long_to_bytes
from gmpy2 import mpz, iroot

def hastad_attack(n_list, c_list):
    # Chinese Remainder Theorem
    N = 1
    for n in n_list:
        N *= n
    
    solution = 0
    for n_i, c_i in zip(n_list, c_list):
        Ni = N // n_i
        solution += c_i * Ni * pow(Ni, -1, n_i)
    
    solution %= N
    
    # Cube root
    m, exact = iroot(mpz(solution), 3)
    return long_to_bytes(int(m)) if exact else None

# Replace with actual values from out.txt
n_list = [15339809337985092259354871340311207170187788184701090902108073306795062288803422279149015504552655693138131547020213622526800482438135884661368981514933476512563559114391352211824973569727638221966450961102285280779178114452670480644158117754434778596849490669058248471620784953158285709603239202669295394100916763221313908843178663798110344428711452384797116239510206451755412390810155029599182034280299499359647720768576579108712010823268798559249274635671343450704843971000237014150847920308944612572129265079069357277769903042033065441575111938925776427845640249774722402201432576031400856754081063880209573709999, 18082283313933256673492246630856535363007783359017993209046213969804478738574633270586186511930928902315627384730269268671536791563912789149985537680128140449016675557478345570435702955284629509000609405576316132524015698859125990457155175643063419012707171601623240796765883487929572317784941650703670119204470185972726428566754272441851580097494882990979555769593856615646728684261864022280926637548824712028623901248187376485156040115132551783317952997683646298339772013425722247635760886760247974804005500657847726696317367807329591170674214394090731980912067645113117212543604915605759407517842650327785890255343, 23784435623820886393476445560347735873664059122585757276409402341742968267254847547291458327358374956429907395861774090292174450234082438068688553004706502444300968268368535546442847480445347616944134964271153107046444727487876686932134828730299228564266437074846285694566700004662435550354419171884933649187005353905748124126702629261728420795100940856534584020056554193634909059076688659748440413882768933230849170227658859421869918308610917896314138674170093052299667173278778901015577462596270304589175944097716145817113614195255368275926981153915475854662785110328489764222838540940280526644590288761347976942949]
c_list = [7233823574053772526357322993079592662423422526055182657553159649458431667971071096938122791961128115022704656253731605910630740655039850229610231650052277922752613042075827977798576429256899071809448178860266191944149400077152670645393827352880196521310776282405515299072518422043889422740062362667647529778735405485835719854143495175908005171182407711664683509924897751410318194566386033359436275730539226963578867813683101778108181605960957418022172486705631467881149038620090186614032887185046917548995327603088507764911976643487651922106752753391433906177766296103913638884784592305162292674312025888382472170561, 17397856115429006346555844701037853206678062977701478539815758408165005798026079058674911380951007140580886785790248492703968526396887292109820689023677665824231913637772249680460451036717907504664374208016344306935478100027241667344866514239810303425267315837305697186779178441682973753864161730741142697192840808676267287742672290951277325994009232491694215579480828079194677632067793491478764120098886751660439090603900200040223555537936930755297821763733049796160286169807705257967943548559578662371982072118969146714531167549026294845682627325717766016382051885341737938524855496717745086438189230072408941823216, 13773013989515406265613716500356781557743686513033572498728603621523393062608996349590742112956397595374788102707348208490958753911133742327584096382663024800033781260013381068868829323484350724918217893800834498073568935271606957446484986229548056055277458713034323612416650207396068615311711960034583604045887100040953793977984965345785613933485872698323257782114750741924091202589718967501012420125444199665953645200919335085965058873534972740120771673320674532297101420381643171180568612501030475640806277365356218096353609164748940510041243475482626125028065825905467722267106147160431187427642049604559575803480]
print(hastad_attack(n_list, c_list))
