
import pandas as pd
import numpy as np
from torch import nn
import torch
from torch import tensor
#데이터 입력 pandas를 이용 
data_path='/var/data-01-test-score.csv'
#data=np.loadtxt(data_path, delimiter=',', dtype=np.float32)
data=pd.read_csv(data_path, header=None, dtype=np.float32)
#x, y 데이터 tensor에 저장
…for epoch in range(1000):#학습 1000번

    y_pred = model(x_data)#xdata를 입력하여 y예측값 출력
    b=a(y_pred, y_data)
    loss = criterion(y_pred, y_data)#손실함수 계산하여 저장
    print(f'Epoch: {epoch} | Loss: {loss.item()} ')#f_string {}안의 값은 변수이
    optimizer.zero_grad()#기울기의 값이 누적되기 때문에 기울기 값을 0으로 만들어준다
    loss.backward()#역전파를 실행하여 손실 함수를 미분하여 계산
    optimizer.step()#step함수를 통해 w와 b의 값을 바꿈

################################################
Epoch: 0 | Loss: 18256.181640625 
Epoch: 1 | Loss: 6757.38623046875 
Epoch: 2 | Loss: 2505.96044921875 
Epoch: 3 | Loss: 934.0879516601562 
Epoch: 4 | Loss: 352.9198913574219 
Epoch: 5 | Loss: 138.04312133789062 
Epoch: 6 | Loss: 58.5941047668457 
Epoch: 7 | Loss: 29.216590881347656 
Epoch: 8 | Loss: 18.35192108154297 
Epoch: 9 | Loss: 14.331923484802246 
Epoch: 10 | Loss: 12.842635154724121 
Epoch: 11 | Loss: 12.288989067077637 
Epoch: 12 | Loss: 12.081311225891113 
Epoch: 13 | Loss: 12.001520156860352 
Epoch: 14 | Loss: 11.969038009643555 
Epoch: 15 | Loss: 11.954024314880371 
Epoch: 16 | Loss: 11.945483207702637 
Epoch: 17 | Loss: 11.939347267150879 
Epoch: 18 | Loss: 11.934089660644531 
Epoch: 19 | Loss: 11.929162979125977 
Epoch: 20 | Loss: 11.9243745803833 
Epoch: 21 | Loss: 11.919620513916016 
Epoch: 22 | Loss: 11.914883613586426 
Epoch: 23 | Loss: 11.910170555114746 
Epoch: 24 | Loss: 11.905445098876953 
Epoch: 25 | Loss: 11.900739669799805 
Epoch: 26 | Loss: 11.896039962768555 
Epoch: 27 | Loss: 11.891345024108887 
Epoch: 28 | Loss: 11.886662483215332 
Epoch: 29 | Loss: 11.88195514678955 
Epoch: 30 | Loss: 11.877266883850098 
Epoch: 31 | Loss: 11.872588157653809 
Epoch: 32 | Loss: 11.867908477783203 
Epoch: 33 | Loss: 11.8632230758667 
Epoch: 34 | Loss: 11.858551025390625 
Epoch: 35 | Loss: 11.853878021240234 
Epoch: 36 | Loss: 11.84920883178711 
Epoch: 37 | Loss: 11.844560623168945 
Epoch: 38 | Loss: 11.839897155761719 
Epoch: 39 | Loss: 11.835244178771973 
Epoch: 40 | Loss: 11.830601692199707 
Epoch: 41 | Loss: 11.825959205627441 
Epoch: 42 | Loss: 11.821333885192871 
Epoch: 43 | Loss: 11.816678047180176 
Epoch: 44 | Loss: 11.812047958374023 
Epoch: 45 | Loss: 11.807417869567871 
Epoch: 46 | Loss: 11.802790641784668 
Epoch: 47 | Loss: 11.798178672790527 
Epoch: 48 | Loss: 11.793549537658691 
Epoch: 49 | Loss: 11.788939476013184 
Epoch: 50 | Loss: 11.784326553344727 
Epoch: 51 | Loss: 11.779725074768066 
Epoch: 52 | Loss: 11.775121688842773 
Epoch: 53 | Loss: 11.770525932312012 
Epoch: 54 | Loss: 11.765937805175781 
Epoch: 55 | Loss: 11.761346817016602 
Epoch: 56 | Loss: 11.756753921508789 
Epoch: 57 | Loss: 11.75217056274414 
Epoch: 58 | Loss: 11.747607231140137 
Epoch: 59 | Loss: 11.743027687072754 
Epoch: 60 | Loss: 11.738451957702637 
Epoch: 61 | Loss: 11.733874320983887 
Epoch: 62 | Loss: 11.729317665100098 
Epoch: 63 | Loss: 11.724754333496094 
Epoch: 64 | Loss: 11.720209121704102 
Epoch: 65 | Loss: 11.71566390991211 
Epoch: 66 | Loss: 11.711106300354004 
Epoch: 67 | Loss: 11.706555366516113 
Epoch: 68 | Loss: 11.702016830444336 
Epoch: 69 | Loss: 11.697478294372559 
Epoch: 70 | Loss: 11.692946434020996 
Epoch: 71 | Loss: 11.688416481018066 
Epoch: 72 | Loss: 11.683891296386719 
Epoch: 73 | Loss: 11.679377555847168 
Epoch: 74 | Loss: 11.6748685836792 
Epoch: 75 | Loss: 11.670336723327637 
Epoch: 76 | Loss: 11.665826797485352 
Epoch: 77 | Loss: 11.66132926940918 
Epoch: 78 | Loss: 11.656813621520996 
Epoch: 79 | Loss: 11.652339935302734 
Epoch: 80 | Loss: 11.647839546203613 
Epoch: 81 | Loss: 11.64333724975586 
Epoch: 82 | Loss: 11.63885498046875 
Epoch: 83 | Loss: 11.634378433227539 
Epoch: 84 | Loss: 11.629894256591797 
Epoch: 85 | Loss: 11.6254301071167 
Epoch: 86 | Loss: 11.620945930480957 
Epoch: 87 | Loss: 11.616488456726074 
Epoch: 88 | Loss: 11.611994743347168 
Epoch: 89 | Loss: 11.607562065124512 
Epoch: 90 | Loss: 11.603092193603516 
Epoch: 91 | Loss: 11.598645210266113 
Epoch: 92 | Loss: 11.594194412231445 
Epoch: 93 | Loss: 11.589751243591309 
Epoch: 94 | Loss: 11.585306167602539 
Epoch: 95 | Loss: 11.580867767333984 
Epoch: 96 | Loss: 11.576438903808594 
Epoch: 97 | Loss: 11.571995735168457 
Epoch: 98 | Loss: 11.567584037780762 
Epoch: 99 | Loss: 11.563166618347168 
Epoch: 100 | Loss: 11.558737754821777 
Epoch: 101 | Loss: 11.554328918457031 
Epoch: 102 | Loss: 11.549909591674805 
Epoch: 103 | Loss: 11.545495986938477 
Epoch: 104 | Loss: 11.54109001159668 
Epoch: 105 | Loss: 11.536704063415527 
Epoch: 106 | Loss: 11.532293319702148 
Epoch: 107 | Loss: 11.527917861938477 
Epoch: 108 | Loss: 11.523514747619629 
Epoch: 109 | Loss: 11.51913070678711 
Epoch: 110 | Loss: 11.514753341674805 
Epoch: 111 | Loss: 11.510356903076172 
Epoch: 112 | Loss: 11.505995750427246 
Epoch: 113 | Loss: 11.501628875732422 
Epoch: 114 | Loss: 11.497258186340332 
Epoch: 115 | Loss: 11.492901802062988 
Epoch: 116 | Loss: 11.488543510437012 
Epoch: 117 | Loss: 11.4841890335083 
Epoch: 118 | Loss: 11.479811668395996 
Epoch: 119 | Loss: 11.475482940673828 
Epoch: 120 | Loss: 11.471142768859863 
Epoch: 121 | Loss: 11.466787338256836 
Epoch: 122 | Loss: 11.462449073791504 
Epoch: 123 | Loss: 11.458121299743652 
Epoch: 124 | Loss: 11.4537935256958 
Epoch: 125 | Loss: 11.449458122253418 
Epoch: 126 | Loss: 11.445143699645996 
Epoch: 127 | Loss: 11.440814971923828 
Epoch: 128 | Loss: 11.436509132385254 
Epoch: 129 | Loss: 11.432186126708984 
Epoch: 130 | Loss: 11.42788314819336 
Epoch: 131 | Loss: 11.423566818237305 
Epoch: 132 | Loss: 11.419275283813477 
Epoch: 133 | Loss: 11.414970397949219 
Epoch: 134 | Loss: 11.41067886352539 
Epoch: 135 | Loss: 11.40639877319336 
Epoch: 136 | Loss: 11.402099609375 
Epoch: 137 | Loss: 11.397834777832031 
Epoch: 138 | Loss: 11.393535614013672 
Epoch: 139 | Loss: 11.389259338378906 
Epoch: 140 | Loss: 11.384984970092773 
Epoch: 141 | Loss: 11.380715370178223 
Epoch: 142 | Loss: 11.376461029052734 
Epoch: 143 | Loss: 11.3721923828125 
Epoch: 144 | Loss: 11.367918968200684 
Epoch: 145 | Loss: 11.363670349121094 
Epoch: 146 | Loss: 11.359417915344238 
Epoch: 147 | Loss: 11.355177879333496 
Epoch: 148 | Loss: 11.350934028625488 
Epoch: 149 | Loss: 11.346693992614746 
Epoch: 150 | Loss: 11.342446327209473 
Epoch: 151 | Loss: 11.338227272033691 
Epoch: 152 | Loss: 11.333992004394531 
Epoch: 153 | Loss: 11.329767227172852 
Epoch: 154 | Loss: 11.325542449951172 
Epoch: 155 | Loss: 11.321320533752441 
Epoch: 156 | Loss: 11.317105293273926 
Epoch: 157 | Loss: 11.312904357910156 
Epoch: 158 | Loss: 11.308691024780273 
Epoch: 159 | Loss: 11.304491996765137 
Epoch: 160 | Loss: 11.300275802612305 
Epoch: 161 | Loss: 11.296089172363281 
Epoch: 162 | Loss: 11.291884422302246 
Epoch: 163 | Loss: 11.287702560424805 
Epoch: 164 | Loss: 11.283519744873047 
Epoch: 165 | Loss: 11.279333114624023 
Epoch: 166 | Loss: 11.275141716003418 
Epoch: 167 | Loss: 11.270960807800293 
Epoch: 168 | Loss: 11.266801834106445 
Epoch: 169 | Loss: 11.262629508972168 
Epoch: 170 | Loss: 11.258471488952637 
Epoch: 171 | Loss: 11.254293441772461 
Epoch: 172 | Loss: 11.250144004821777 
Epoch: 173 | Loss: 11.245985984802246 
Epoch: 174 | Loss: 11.241839408874512 
Epoch: 175 | Loss: 11.237675666809082 
Epoch: 176 | Loss: 11.233525276184082 
Epoch: 177 | Loss: 11.229391098022461 
Epoch: 178 | Loss: 11.225262641906738 
Epoch: 179 | Loss: 11.221135139465332 
Epoch: 180 | Loss: 11.21699333190918 
Epoch: 181 | Loss: 11.212860107421875 
Epoch: 182 | Loss: 11.208736419677734 
Epoch: 183 | Loss: 11.20461654663086 
Epoch: 184 | Loss: 11.200496673583984 
Epoch: 185 | Loss: 11.196383476257324 
Epoch: 186 | Loss: 11.192268371582031 
Epoch: 187 | Loss: 11.188162803649902 
Epoch: 188 | Loss: 11.184054374694824 
Epoch: 189 | Loss: 11.179973602294922 
Epoch: 190 | Loss: 11.175875663757324 
Epoch: 191 | Loss: 11.17176628112793 
Epoch: 192 | Loss: 11.167679786682129 
Epoch: 193 | Loss: 11.163593292236328 
Epoch: 194 | Loss: 11.159512519836426 
Epoch: 195 | Loss: 11.155440330505371 
Epoch: 196 | Loss: 11.151362419128418 
Epoch: 197 | Loss: 11.147292137145996 
Epoch: 198 | Loss: 11.143213272094727 
Epoch: 199 | Loss: 11.139145851135254 
Epoch: 200 | Loss: 11.135100364685059 
Epoch: 201 | Loss: 11.131041526794434 
Epoch: 202 | Loss: 11.126977920532227 
Epoch: 203 | Loss: 11.122937202453613 
Epoch: 204 | Loss: 11.118868827819824 
Epoch: 205 | Loss: 11.114829063415527 
Epoch: 206 | Loss: 11.110787391662598 
Epoch: 207 | Loss: 11.1067533493042 
Epoch: 208 | Loss: 11.102707862854004 
Epoch: 209 | Loss: 11.098670959472656 
Epoch: 210 | Loss: 11.094644546508789 
Epoch: 211 | Loss: 11.090636253356934 
Epoch: 212 | Loss: 11.086604118347168 
Epoch: 213 | Loss: 11.082594871520996 
Epoch: 214 | Loss: 11.078569412231445 
Epoch: 215 | Loss: 11.074563026428223 
Epoch: 216 | Loss: 11.070556640625 
Epoch: 217 | Loss: 11.066557884216309 
Epoch: 218 | Loss: 11.062546730041504 
Epoch: 219 | Loss: 11.058548927307129 
Epoch: 220 | Loss: 11.054553031921387 
Epoch: 221 | Loss: 11.050567626953125 
Epoch: 222 | Loss: 11.04658317565918 
Epoch: 223 | Loss: 11.04259967803955 
Epoch: 224 | Loss: 11.038617134094238 
Epoch: 225 | Loss: 11.03464126586914 
Epoch: 226 | Loss: 11.030657768249512 
Epoch: 227 | Loss: 11.026694297790527 
Epoch: 228 | Loss: 11.022722244262695 
Epoch: 229 | Loss: 11.018759727478027 
Epoch: 230 | Loss: 11.014791488647461 
Epoch: 231 | Loss: 11.01083755493164 
Epoch: 232 | Loss: 11.006884574890137 
Epoch: 233 | Loss: 11.002933502197266 
Epoch: 234 | Loss: 10.998979568481445 
Epoch: 235 | Loss: 10.995035171508789 
Epoch: 236 | Loss: 10.991101264953613 
Epoch: 237 | Loss: 10.987153053283691 
Epoch: 238 | Loss: 10.983233451843262 
Epoch: 239 | Loss: 10.979301452636719 
Epoch: 240 | Loss: 10.97537612915039 
Epoch: 241 | Loss: 10.971449851989746 
Epoch: 242 | Loss: 10.967516899108887 
Epoch: 243 | Loss: 10.963605880737305 
Epoch: 244 | Loss: 10.959687232971191 
Epoch: 245 | Loss: 10.95577621459961 
Epoch: 246 | Loss: 10.951872825622559 
Epoch: 247 | Loss: 10.94796371459961 
Epoch: 248 | Loss: 10.944067001342773 
Epoch: 249 | Loss: 10.940160751342773 
Epoch: 250 | Loss: 10.936269760131836 
Epoch: 251 | Loss: 10.932373046875 
Epoch: 252 | Loss: 10.928474426269531 
Epoch: 253 | Loss: 10.924617767333984 
Epoch: 254 | Loss: 10.9207181930542 
Epoch: 255 | Loss: 10.916840553283691 
Epoch: 256 | Loss: 10.912964820861816 
Epoch: 257 | Loss: 10.909093856811523 
Epoch: 258 | Loss: 10.905226707458496 
Epoch: 259 | Loss: 10.901352882385254 
Epoch: 260 | Loss: 10.897496223449707 
Epoch: 261 | Loss: 10.893637657165527 
Epoch: 262 | Loss: 10.889776229858398 
Epoch: 263 | Loss: 10.8859224319458 
Epoch: 264 | Loss: 10.882083892822266 
Epoch: 265 | Loss: 10.8782377243042 
Epoch: 266 | Loss: 10.8743896484375 
Epoch: 267 | Loss: 10.870555877685547 
Epoch: 268 | Loss: 10.866717338562012 
Epoch: 269 | Loss: 10.862870216369629 
Epoch: 270 | Loss: 10.859036445617676 
Epoch: 271 | Loss: 10.855220794677734 
Epoch: 272 | Loss: 10.851404190063477 
Epoch: 273 | Loss: 10.847590446472168 
Epoch: 274 | Loss: 10.843750953674316 
Epoch: 275 | Loss: 10.839958190917969 
Epoch: 276 | Loss: 10.836142539978027 
Epoch: 277 | Loss: 10.832340240478516 
Epoch: 278 | Loss: 10.828522682189941 
Epoch: 279 | Loss: 10.824726104736328 
Epoch: 280 | Loss: 10.820934295654297 
Epoch: 281 | Loss: 10.817129135131836 
Epoch: 282 | Loss: 10.813335418701172 
Epoch: 283 | Loss: 10.809556007385254 
Epoch: 284 | Loss: 10.805761337280273 
Epoch: 285 | Loss: 10.801982879638672 
Epoch: 286 | Loss: 10.798226356506348 
Epoch: 287 | Loss: 10.794429779052734 
Epoch: 288 | Loss: 10.790666580200195 
Epoch: 289 | Loss: 10.786887168884277 
Epoch: 290 | Loss: 10.783114433288574 
Epoch: 291 | Loss: 10.77935791015625 
Epoch: 292 | Loss: 10.775601387023926 
Epoch: 293 | Loss: 10.771833419799805 
Epoch: 294 | Loss: 10.768085479736328 
Epoch: 295 | Loss: 10.764339447021484 
Epoch: 296 | Loss: 10.760599136352539 
Epoch: 297 | Loss: 10.756843566894531 
Epoch: 298 | Loss: 10.75311279296875 
Epoch: 299 | Loss: 10.749364852905273 
Epoch: 300 | Loss: 10.745647430419922 
Epoch: 301 | Loss: 10.741901397705078 
Epoch: 302 | Loss: 10.738171577453613 
Epoch: 303 | Loss: 10.734436988830566 
Epoch: 304 | Loss: 10.730713844299316 
Epoch: 305 | Loss: 10.726999282836914 
Epoch: 306 | Loss: 10.723285675048828 
Epoch: 307 | Loss: 10.71957015991211 
Epoch: 308 | Loss: 10.715860366821289 
Epoch: 309 | Loss: 10.712153434753418 
Epoch: 310 | Loss: 10.708457946777344 
Epoch: 311 | Loss: 10.704760551452637 
Epoch: 312 | Loss: 10.701059341430664 
Epoch: 313 | Loss: 10.697361946105957 
Epoch: 314 | Loss: 10.693669319152832 
Epoch: 315 | Loss: 10.689985275268555 
Epoch: 316 | Loss: 10.686296463012695 
Epoch: 317 | Loss: 10.68261432647705 
Epoch: 318 | Loss: 10.678938865661621 
Epoch: 319 | Loss: 10.675263404846191 
Epoch: 320 | Loss: 10.671577453613281 
Epoch: 321 | Loss: 10.667916297912598 
Epoch: 322 | Loss: 10.664267539978027 
Epoch: 323 | Loss: 10.660587310791016 
Epoch: 324 | Loss: 10.656940460205078 
Epoch: 325 | Loss: 10.653281211853027 
Epoch: 326 | Loss: 10.649614334106445 
Epoch: 327 | Loss: 10.645968437194824 
Epoch: 328 | Loss: 10.642316818237305 
Epoch: 329 | Loss: 10.638667106628418 
Epoch: 330 | Loss: 10.635034561157227 
Epoch: 331 | Loss: 10.631394386291504 
Epoch: 332 | Loss: 10.627754211425781 
Epoch: 333 | Loss: 10.624119758605957 
Epoch: 334 | Loss: 10.620492935180664 
Epoch: 335 | Loss: 10.616872787475586 
Epoch: 336 | Loss: 10.613239288330078 
Epoch: 337 | Loss: 10.609623908996582 
Epoch: 338 | Loss: 10.606000900268555 
Epoch: 339 | Loss: 10.602392196655273 
Epoch: 340 | Loss: 10.598779678344727 
Epoch: 341 | Loss: 10.595166206359863 
Epoch: 342 | Loss: 10.591568946838379 
Epoch: 343 | Loss: 10.587967872619629 
Epoch: 344 | Loss: 10.584362983703613 
Epoch: 345 | Loss: 10.580768585205078 
Epoch: 346 | Loss: 10.577166557312012 
Epoch: 347 | Loss: 10.573592185974121 
Epoch: 348 | Loss: 10.569988250732422 
Epoch: 349 | Loss: 10.566418647766113 
Epoch: 350 | Loss: 10.56283187866211 
Epoch: 351 | Loss: 10.559247970581055 
Epoch: 352 | Loss: 10.555668830871582 
Epoch: 353 | Loss: 10.552093505859375 
Epoch: 354 | Loss: 10.548537254333496 
Epoch: 355 | Loss: 10.544979095458984 
Epoch: 356 | Loss: 10.541421890258789 
Epoch: 357 | Loss: 10.537841796875 
Epoch: 358 | Loss: 10.534284591674805 
Epoch: 359 | Loss: 10.530739784240723 
Epoch: 360 | Loss: 10.527177810668945 
Epoch: 361 | Loss: 10.523625373840332 
Epoch: 362 | Loss: 10.520097732543945 
Epoch: 363 | Loss: 10.516550064086914 
Epoch: 364 | Loss: 10.5130033493042 
Epoch: 365 | Loss: 10.509471893310547 
Epoch: 366 | Loss: 10.50593376159668 
Epoch: 367 | Loss: 10.502403259277344 
Epoch: 368 | Loss: 10.498866081237793 
Epoch: 369 | Loss: 10.495351791381836 
Epoch: 370 | Loss: 10.491835594177246 
Epoch: 371 | Loss: 10.488306045532227 
Epoch: 372 | Loss: 10.484807014465332 
Epoch: 373 | Loss: 10.481280326843262 
Epoch: 374 | Loss: 10.477779388427734 
Epoch: 375 | Loss: 10.474260330200195 
Epoch: 376 | Loss: 10.470760345458984 
Epoch: 377 | Loss: 10.467253684997559 
Epoch: 378 | Loss: 10.463756561279297 
Epoch: 379 | Loss: 10.4602689743042 
Epoch: 380 | Loss: 10.456777572631836 
Epoch: 381 | Loss: 10.45329475402832 
Epoch: 382 | Loss: 10.44979476928711 
Epoch: 383 | Loss: 10.446310043334961 
Epoch: 384 | Loss: 10.442829132080078 
Epoch: 385 | Loss: 10.439350128173828 
Epoch: 386 | Loss: 10.435877799987793 
Epoch: 387 | Loss: 10.432419776916504 
Epoch: 388 | Loss: 10.428934097290039 
Epoch: 389 | Loss: 10.4254789352417 
Epoch: 390 | Loss: 10.422028541564941 
Epoch: 391 | Loss: 10.418564796447754 
Epoch: 392 | Loss: 10.415105819702148 
Epoch: 393 | Loss: 10.411646842956543 
Epoch: 394 | Loss: 10.408191680908203 
Epoch: 395 | Loss: 10.404738426208496 
Epoch: 396 | Loss: 10.401302337646484 
Epoch: 397 | Loss: 10.397852897644043 
Epoch: 398 | Loss: 10.394421577453613 
Epoch: 399 | Loss: 10.390972137451172 
Epoch: 400 | Loss: 10.387537002563477 
Epoch: 401 | Loss: 10.384119987487793 
Epoch: 402 | Loss: 10.380684852600098 
Epoch: 403 | Loss: 10.377257347106934 
Epoch: 404 | Loss: 10.373845100402832 
Epoch: 405 | Loss: 10.3704252243042 
Epoch: 406 | Loss: 10.367003440856934 
Epoch: 407 | Loss: 10.363576889038086 
Epoch: 408 | Loss: 10.360169410705566 
Epoch: 409 | Loss: 10.356762886047363 
Epoch: 410 | Loss: 10.353358268737793 
Epoch: 411 | Loss: 10.349950790405273 
Epoch: 412 | Loss: 10.346558570861816 
Epoch: 413 | Loss: 10.343155860900879 
Epoch: 414 | Loss: 10.339773178100586 
Epoch: 415 | Loss: 10.336369514465332 
Epoch: 416 | Loss: 10.332986831665039 
Epoch: 417 | Loss: 10.329608917236328 
Epoch: 418 | Loss: 10.326210021972656 
Epoch: 419 | Loss: 10.322834014892578 
Epoch: 420 | Loss: 10.319445610046387 
Epoch: 421 | Loss: 10.316082000732422 
Epoch: 422 | Loss: 10.312712669372559 
Epoch: 423 | Loss: 10.309333801269531 
Epoch: 424 | Loss: 10.305968284606934 
Epoch: 425 | Loss: 10.3026123046875 
Epoch: 426 | Loss: 10.299249649047852 
Epoch: 427 | Loss: 10.29589557647705 
Epoch: 428 | Loss: 10.292540550231934 
Epoch: 429 | Loss: 10.2891845703125 
Epoch: 430 | Loss: 10.285833358764648 
Epoch: 431 | Loss: 10.282495498657227 
Epoch: 432 | Loss: 10.279152870178223 
Epoch: 433 | Loss: 10.275799751281738 
Epoch: 434 | Loss: 10.27246379852295 
Epoch: 435 | Loss: 10.269133567810059 
Epoch: 436 | Loss: 10.2658052444458 
Epoch: 437 | Loss: 10.262465476989746 
Epoch: 438 | Loss: 10.25914192199707 
Epoch: 439 | Loss: 10.25581169128418 
Epoch: 440 | Loss: 10.252497673034668 
Epoch: 441 | Loss: 10.249183654785156 
Epoch: 442 | Loss: 10.24587631225586 
Epoch: 443 | Loss: 10.242546081542969 
Epoch: 444 | Loss: 10.239229202270508 
Epoch: 445 | Loss: 10.235931396484375 
Epoch: 446 | Loss: 10.232620239257812 
Epoch: 447 | Loss: 10.229321479797363 
Epoch: 448 | Loss: 10.226025581359863 
Epoch: 449 | Loss: 10.222732543945312 
Epoch: 450 | Loss: 10.219427108764648 
Epoch: 451 | Loss: 10.216133117675781 
Epoch: 452 | Loss: 10.212850570678711 
Epoch: 453 | Loss: 10.209559440612793 
Epoch: 454 | Loss: 10.206281661987305 
Epoch: 455 | Loss: 10.203006744384766 
Epoch: 456 | Loss: 10.199731826782227 
Epoch: 457 | Loss: 10.196449279785156 
Epoch: 458 | Loss: 10.193183898925781 
Epoch: 459 | Loss: 10.18991470336914 
Epoch: 460 | Loss: 10.186639785766602 
Epoch: 461 | Loss: 10.18337631225586 
Epoch: 462 | Loss: 10.180124282836914 
Epoch: 463 | Loss: 10.176861763000488 
Epoch: 464 | Loss: 10.173606872558594 
Epoch: 465 | Loss: 10.170348167419434 
Epoch: 466 | Loss: 10.16711139678955 
Epoch: 467 | Loss: 10.163859367370605 
Epoch: 468 | Loss: 10.160623550415039 
Epoch: 469 | Loss: 10.157378196716309 
Epoch: 470 | Loss: 10.15413761138916 
Epoch: 471 | Loss: 10.150895118713379 
Epoch: 472 | Loss: 10.14767074584961 
Epoch: 473 | Loss: 10.144434928894043 
Epoch: 474 | Loss: 10.141212463378906 
Epoch: 475 | Loss: 10.137982368469238 
Epoch: 476 | Loss: 10.134749412536621 
Epoch: 477 | Loss: 10.131542205810547 
Epoch: 478 | Loss: 10.12833023071289 
Epoch: 479 | Loss: 10.125109672546387 
Epoch: 480 | Loss: 10.1218900680542 
Epoch: 481 | Loss: 10.11867904663086 
Epoch: 482 | Loss: 10.115470886230469 
Epoch: 483 | Loss: 10.11227798461914 
Epoch: 484 | Loss: 10.109078407287598 
Epoch: 485 | Loss: 10.105886459350586 
Epoch: 486 | Loss: 10.102672576904297 
Epoch: 487 | Loss: 10.09949016571045 
Epoch: 488 | Loss: 10.096294403076172 
Epoch: 489 | Loss: 10.093104362487793 
Epoch: 490 | Loss: 10.089929580688477 
Epoch: 491 | Loss: 10.086756706237793 
Epoch: 492 | Loss: 10.083568572998047 
Epoch: 493 | Loss: 10.080371856689453 
Epoch: 494 | Loss: 10.077203750610352 
Epoch: 495 | Loss: 10.074039459228516 
Epoch: 496 | Loss: 10.070869445800781 
Epoch: 497 | Loss: 10.067704200744629 
Epoch: 498 | Loss: 10.064543724060059 
Epoch: 499 | Loss: 10.061388969421387 
Epoch: 500 | Loss: 10.058235168457031 
Epoch: 501 | Loss: 10.055062294006348 
Epoch: 502 | Loss: 10.05191421508789 
Epoch: 503 | Loss: 10.048773765563965 
Epoch: 504 | Loss: 10.045613288879395 
Epoch: 505 | Loss: 10.042459487915039 
Epoch: 506 | Loss: 10.039306640625 
Epoch: 507 | Loss: 10.036175727844238 
Epoch: 508 | Loss: 10.03305721282959 
Epoch: 509 | Loss: 10.029914855957031 
Epoch: 510 | Loss: 10.026782989501953 
Epoch: 511 | Loss: 10.023652076721191 
Epoch: 512 | Loss: 10.020525932312012 
Epoch: 513 | Loss: 10.017400741577148 
Epoch: 514 | Loss: 10.014274597167969 
Epoch: 515 | Loss: 10.011163711547852 
Epoch: 516 | Loss: 10.008047103881836 
Epoch: 517 | Loss: 10.004922866821289 
Epoch: 518 | Loss: 10.001814842224121 
Epoch: 519 | Loss: 9.998710632324219 
Epoch: 520 | Loss: 9.995594024658203 
Epoch: 521 | Loss: 9.992494583129883 
Epoch: 522 | Loss: 9.989385604858398 
Epoch: 523 | Loss: 9.986313819885254 
Epoch: 524 | Loss: 9.9832124710083 
Epoch: 525 | Loss: 9.980107307434082 
Epoch: 526 | Loss: 9.977020263671875 
Epoch: 527 | Loss: 9.973933219909668 
Epoch: 528 | Loss: 9.970850944519043 
Epoch: 529 | Loss: 9.967759132385254 
Epoch: 530 | Loss: 9.964686393737793 
Epoch: 531 | Loss: 9.961607933044434 
Epoch: 532 | Loss: 9.958523750305176 
Epoch: 533 | Loss: 9.955460548400879 
Epoch: 534 | Loss: 9.95237922668457 
Epoch: 535 | Loss: 9.94931697845459 
Epoch: 536 | Loss: 9.946258544921875 
Epoch: 537 | Loss: 9.943201065063477 
Epoch: 538 | Loss: 9.940140724182129 
Epoch: 539 | Loss: 9.937080383300781 
Epoch: 540 | Loss: 9.934024810791016 
Epoch: 541 | Loss: 9.930962562561035 
Epoch: 542 | Loss: 9.927921295166016 
Epoch: 543 | Loss: 9.924864768981934 
Epoch: 544 | Loss: 9.921830177307129 
Epoch: 545 | Loss: 9.918787002563477 
Epoch: 546 | Loss: 9.915749549865723 
Epoch: 547 | Loss: 9.912714004516602 
Epoch: 548 | Loss: 9.909677505493164 
Epoch: 549 | Loss: 9.906645774841309 
Epoch: 550 | Loss: 9.903619766235352 
Epoch: 551 | Loss: 9.900588035583496 
Epoch: 552 | Loss: 9.897578239440918 
Epoch: 553 | Loss: 9.894548416137695 
Epoch: 554 | Loss: 9.891518592834473 
Epoch: 555 | Loss: 9.888514518737793 
Epoch: 556 | Loss: 9.88548469543457 
Epoch: 557 | Loss: 9.882481575012207 
Epoch: 558 | Loss: 9.879476547241211 
Epoch: 559 | Loss: 9.876456260681152 
Epoch: 560 | Loss: 9.873461723327637 
Epoch: 561 | Loss: 9.870452880859375 
Epoch: 562 | Loss: 9.867467880249023 
Epoch: 563 | Loss: 9.864452362060547 
Epoch: 564 | Loss: 9.861468315124512 
Epoch: 565 | Loss: 9.858469009399414 
Epoch: 566 | Loss: 9.855493545532227 
Epoch: 567 | Loss: 9.852502822875977 
Epoch: 568 | Loss: 9.849527359008789 
Epoch: 569 | Loss: 9.846528053283691 
Epoch: 570 | Loss: 9.843559265136719 
Epoch: 571 | Loss: 9.840588569641113 
Epoch: 572 | Loss: 9.837610244750977 
Epoch: 573 | Loss: 9.834625244140625 
Epoch: 574 | Loss: 9.83166790008545 
Epoch: 575 | Loss: 9.828700065612793 
Epoch: 576 | Loss: 9.825736999511719 
Epoch: 577 | Loss: 9.822761535644531 
Epoch: 578 | Loss: 9.819812774658203 
Epoch: 579 | Loss: 9.816855430603027 
Epoch: 580 | Loss: 9.813912391662598 
Epoch: 581 | Loss: 9.810944557189941 
Epoch: 582 | Loss: 9.808001518249512 
Epoch: 583 | Loss: 9.805057525634766 
Epoch: 584 | Loss: 9.802107810974121 
Epoch: 585 | Loss: 9.799159049987793 
Epoch: 586 | Loss: 9.796233177185059 
Epoch: 587 | Loss: 9.793298721313477 
Epoch: 588 | Loss: 9.790360450744629 
Epoch: 589 | Loss: 9.787432670593262 
Epoch: 590 | Loss: 9.784491539001465 
Epoch: 591 | Loss: 9.781557083129883 
Epoch: 592 | Loss: 9.778639793395996 
Epoch: 593 | Loss: 9.775700569152832 
Epoch: 594 | Loss: 9.772805213928223 
Epoch: 595 | Loss: 9.76988410949707 
Epoch: 596 | Loss: 9.766980171203613 
Epoch: 597 | Loss: 9.764059066772461 
Epoch: 598 | Loss: 9.76114273071289 
Epoch: 599 | Loss: 9.75822639465332 
Epoch: 600 | Loss: 9.755337715148926 
Epoch: 601 | Loss: 9.752420425415039 
Epoch: 602 | Loss: 9.749529838562012 
Epoch: 603 | Loss: 9.746630668640137 
Epoch: 604 | Loss: 9.743731498718262 
Epoch: 605 | Loss: 9.7408447265625 
Epoch: 606 | Loss: 9.737948417663574 
Epoch: 607 | Loss: 9.735052108764648 
Epoch: 608 | Loss: 9.73218059539795 
Epoch: 609 | Loss: 9.729293823242188 
Epoch: 610 | Loss: 9.726404190063477 
Epoch: 611 | Loss: 9.723527908325195 
Epoch: 612 | Loss: 9.720667839050293 
Epoch: 613 | Loss: 9.717777252197266 
Epoch: 614 | Loss: 9.7149076461792 
Epoch: 615 | Loss: 9.7120361328125 
Epoch: 616 | Loss: 9.7091703414917 
Epoch: 617 | Loss: 9.706314086914062 
Epoch: 618 | Loss: 9.703448295593262 
Epoch: 619 | Loss: 9.700577735900879 
Epoch: 620 | Loss: 9.697717666625977 
Epoch: 621 | Loss: 9.694890022277832 
Epoch: 622 | Loss: 9.692028999328613 
Epoch: 623 | Loss: 9.689166069030762 
Epoch: 624 | Loss: 9.686314582824707 
Epoch: 625 | Loss: 9.683479309082031 
Epoch: 626 | Loss: 9.680630683898926 
Epoch: 627 | Loss: 9.677791595458984 
Epoch: 628 | Loss: 9.674962043762207 
Epoch: 629 | Loss: 9.672117233276367 
Epoch: 630 | Loss: 9.669280052185059 
Epoch: 631 | Loss: 9.666461944580078 
Epoch: 632 | Loss: 9.663617134094238 
Epoch: 633 | Loss: 9.660794258117676 
Epoch: 634 | Loss: 9.657973289489746 
Epoch: 635 | Loss: 9.655155181884766 
Epoch: 636 | Loss: 9.652326583862305 
Epoch: 637 | Loss: 9.649517059326172 
Epoch: 638 | Loss: 9.646702766418457 
Epoch: 639 | Loss: 9.643898010253906 
Epoch: 640 | Loss: 9.641071319580078 
Epoch: 641 | Loss: 9.63826847076416 
Epoch: 642 | Loss: 9.63546085357666 
Epoch: 643 | Loss: 9.632665634155273 
Epoch: 644 | Loss: 9.62985610961914 
Epoch: 645 | Loss: 9.627056121826172 
Epoch: 646 | Loss: 9.624277114868164 
Epoch: 647 | Loss: 9.621476173400879 
Epoch: 648 | Loss: 9.618685722351074 
Epoch: 649 | Loss: 9.61589241027832 
Epoch: 650 | Loss: 9.61309814453125 
Epoch: 651 | Loss: 9.610321998596191 
Epoch: 652 | Loss: 9.607542991638184 
Epoch: 653 | Loss: 9.604761123657227 
Epoch: 654 | Loss: 9.601977348327637 
Epoch: 655 | Loss: 9.599214553833008 
Epoch: 656 | Loss: 9.596435546875 
Epoch: 657 | Loss: 9.593674659729004 
Epoch: 658 | Loss: 9.590887069702148 
Epoch: 659 | Loss: 9.588125228881836 
Epoch: 660 | Loss: 9.585367202758789 
Epoch: 661 | Loss: 9.582599639892578 
Epoch: 662 | Loss: 9.579842567443848 
Epoch: 663 | Loss: 9.577088356018066 
Epoch: 664 | Loss: 9.574336051940918 
Epoch: 665 | Loss: 9.571581840515137 
Epoch: 666 | Loss: 9.568826675415039 
Epoch: 667 | Loss: 9.566078186035156 
Epoch: 668 | Loss: 9.56334400177002 
Epoch: 669 | Loss: 9.56059455871582 
Epoch: 670 | Loss: 9.557845115661621 
Epoch: 671 | Loss: 9.555105209350586 
Epoch: 672 | Loss: 9.552386283874512 
Epoch: 673 | Loss: 9.549649238586426 
Epoch: 674 | Loss: 9.546923637390137 
Epoch: 675 | Loss: 9.544183731079102 
Epoch: 676 | Loss: 9.54145336151123 
Epoch: 677 | Loss: 9.538734436035156 
Epoch: 678 | Loss: 9.536009788513184 
Epoch: 679 | Loss: 9.533297538757324 
Epoch: 680 | Loss: 9.530560493469238 
Epoch: 681 | Loss: 9.527853012084961 
Epoch: 682 | Loss: 9.525146484375 
Epoch: 683 | Loss: 9.522436141967773 
Epoch: 684 | Loss: 9.519720077514648 
Epoch: 685 | Loss: 9.517011642456055 
Epoch: 686 | Loss: 9.514305114746094 
Epoch: 687 | Loss: 9.511604309082031 
Epoch: 688 | Loss: 9.50891399383545 
Epoch: 689 | Loss: 9.50620174407959 
Epoch: 690 | Loss: 9.503520011901855 
Epoch: 691 | Loss: 9.500826835632324 
Epoch: 692 | Loss: 9.49811840057373 
Epoch: 693 | Loss: 9.495448112487793 
Epoch: 694 | Loss: 9.492757797241211 
Epoch: 695 | Loss: 9.490077018737793 
Epoch: 696 | Loss: 9.487397193908691 
Epoch: 697 | Loss: 9.48471450805664 
Epoch: 698 | Loss: 9.482040405273438 
Epoch: 699 | Loss: 9.479361534118652 
Epoch: 700 | Loss: 9.476688385009766 
Epoch: 701 | Loss: 9.474013328552246 
Epoch: 702 | Loss: 9.471351623535156 
Epoch: 703 | Loss: 9.468681335449219 
Epoch: 704 | Loss: 9.466011047363281 
Epoch: 705 | Loss: 9.46335220336914 
Epoch: 706 | Loss: 9.46069049835205 
Epoch: 707 | Loss: 9.45804214477539 
Epoch: 708 | Loss: 9.455379486083984 
Epoch: 709 | Loss: 9.452727317810059 
Epoch: 710 | Loss: 9.450082778930664 
Epoch: 711 | Loss: 9.447426795959473 
Epoch: 712 | Loss: 9.444772720336914 
Epoch: 713 | Loss: 9.44213581085205 
Epoch: 714 | Loss: 9.439496040344238 
Epoch: 715 | Loss: 9.436849594116211 
Epoch: 716 | Loss: 9.434223175048828 
Epoch: 717 | Loss: 9.43157958984375 
Epoch: 718 | Loss: 9.428945541381836 
Epoch: 719 | Loss: 9.426319122314453 
Epoch: 720 | Loss: 9.423686027526855 
Epoch: 721 | Loss: 9.421058654785156 
Epoch: 722 | Loss: 9.418439865112305 
Epoch: 723 | Loss: 9.415823936462402 
Epoch: 724 | Loss: 9.413193702697754 
Epoch: 725 | Loss: 9.41057300567627 
Epoch: 726 | Loss: 9.407958984375 
Epoch: 727 | Loss: 9.405342102050781 
Epoch: 728 | Loss: 9.402741432189941 
Epoch: 729 | Loss: 9.400121688842773 
Epoch: 730 | Loss: 9.397518157958984 
Epoch: 731 | Loss: 9.394903182983398 
Epoch: 732 | Loss: 9.392313957214355 
Epoch: 733 | Loss: 9.389715194702148 
Epoch: 734 | Loss: 9.387115478515625 
Epoch: 735 | Loss: 9.384511947631836 
Epoch: 736 | Loss: 9.381921768188477 
Epoch: 737 | Loss: 9.379332542419434 
Epoch: 738 | Loss: 9.376726150512695 
Epoch: 739 | Loss: 9.374154090881348 
Epoch: 740 | Loss: 9.371562957763672 
Epoch: 741 | Loss: 9.368985176086426 
Epoch: 742 | Loss: 9.36640739440918 
Epoch: 743 | Loss: 9.363824844360352 
Epoch: 744 | Loss: 9.361246109008789 
Epoch: 745 | Loss: 9.358674049377441 
Epoch: 746 | Loss: 9.356090545654297 
Epoch: 747 | Loss: 9.353532791137695 
Epoch: 748 | Loss: 9.350953102111816 
Epoch: 749 | Loss: 9.348392486572266 
Epoch: 750 | Loss: 9.345829010009766 
Epoch: 751 | Loss: 9.343262672424316 
Epoch: 752 | Loss: 9.340710639953613 
Epoch: 753 | Loss: 9.33814811706543 
Epoch: 754 | Loss: 9.335602760314941 
Epoch: 755 | Loss: 9.333049774169922 
Epoch: 756 | Loss: 9.330484390258789 
Epoch: 757 | Loss: 9.327946662902832 
Epoch: 758 | Loss: 9.325390815734863 
Epoch: 759 | Loss: 9.322848320007324 
Epoch: 760 | Loss: 9.32029914855957 
Epoch: 761 | Loss: 9.317760467529297 
Epoch: 762 | Loss: 9.315220832824707 
Epoch: 763 | Loss: 9.312699317932129 
Epoch: 764 | Loss: 9.310168266296387 
Epoch: 765 | Loss: 9.307626724243164 
Epoch: 766 | Loss: 9.305088996887207 
Epoch: 767 | Loss: 9.302557945251465 
Epoch: 768 | Loss: 9.300052642822266 
Epoch: 769 | Loss: 9.29751205444336 
Epoch: 770 | Loss: 9.295001029968262 
Epoch: 771 | Loss: 9.292464256286621 
Epoch: 772 | Loss: 9.289956092834473 
Epoch: 773 | Loss: 9.287446022033691 
Epoch: 774 | Loss: 9.284917831420898 
Epoch: 775 | Loss: 9.282413482666016 
Epoch: 776 | Loss: 9.27990436553955 
Epoch: 777 | Loss: 9.277392387390137 
Epoch: 778 | Loss: 9.274885177612305 
Epoch: 779 | Loss: 9.272385597229004 
Epoch: 780 | Loss: 9.269885063171387 
Epoch: 781 | Loss: 9.267382621765137 
Epoch: 782 | Loss: 9.264892578125 
Epoch: 783 | Loss: 9.262391090393066 
Epoch: 784 | Loss: 9.259899139404297 
Epoch: 785 | Loss: 9.257408142089844 
Epoch: 786 | Loss: 9.254934310913086 
Epoch: 787 | Loss: 9.252432823181152 
Epoch: 788 | Loss: 9.249957084655762 
Epoch: 789 | Loss: 9.247464179992676 
Epoch: 790 | Loss: 9.244994163513184 
Epoch: 791 | Loss: 9.242518424987793 
Epoch: 792 | Loss: 9.240039825439453 
Epoch: 793 | Loss: 9.237565040588379 
Epoch: 794 | Loss: 9.235091209411621 
Epoch: 795 | Loss: 9.232629776000977 
Epoch: 796 | Loss: 9.230146408081055 
Epoch: 797 | Loss: 9.227683067321777 
Epoch: 798 | Loss: 9.22521686553955 
Epoch: 799 | Loss: 9.222747802734375 
Epoch: 800 | Loss: 9.220296859741211 
Epoch: 801 | Loss: 9.217838287353516 
Epoch: 802 | Loss: 9.215380668640137 
Epoch: 803 | Loss: 9.212935447692871 
Epoch: 804 | Loss: 9.210491180419922 
Epoch: 805 | Loss: 9.208040237426758 
Epoch: 806 | Loss: 9.205582618713379 
Epoch: 807 | Loss: 9.203142166137695 
Epoch: 808 | Loss: 9.200701713562012 
Epoch: 809 | Loss: 9.198254585266113 
Epoch: 810 | Loss: 9.195823669433594 
Epoch: 811 | Loss: 9.193378448486328 
Epoch: 812 | Loss: 9.190942764282227 
Epoch: 813 | Loss: 9.18850040435791 
Epoch: 814 | Loss: 9.186086654663086 
Epoch: 815 | Loss: 9.183658599853516 
Epoch: 816 | Loss: 9.18124008178711 
Epoch: 817 | Loss: 9.178792953491211 
Epoch: 818 | Loss: 9.176377296447754 
Epoch: 819 | Loss: 9.173946380615234 
Epoch: 820 | Loss: 9.171545028686523 
Epoch: 821 | Loss: 9.169118881225586 
Epoch: 822 | Loss: 9.166703224182129 
Epoch: 823 | Loss: 9.164302825927734 
Epoch: 824 | Loss: 9.161873817443848 
Epoch: 825 | Loss: 9.159472465515137 
Epoch: 826 | Loss: 9.157051086425781 
Epoch: 827 | Loss: 9.154654502868652 
Epoch: 828 | Loss: 9.152252197265625 
Epoch: 829 | Loss: 9.14986515045166 
Epoch: 830 | Loss: 9.147456169128418 
Epoch: 831 | Loss: 9.145048141479492 
Epoch: 832 | Loss: 9.142655372619629 
Epoch: 833 | Loss: 9.140271186828613 
Epoch: 834 | Loss: 9.137873649597168 
Epoch: 835 | Loss: 9.135493278503418 
Epoch: 836 | Loss: 9.133100509643555 
Epoch: 837 | Loss: 9.130712509155273 
Epoch: 838 | Loss: 9.128339767456055 
Epoch: 839 | Loss: 9.125940322875977 
Epoch: 840 | Loss: 9.123562812805176 
Epoch: 841 | Loss: 9.121197700500488 
Epoch: 842 | Loss: 9.118816375732422 
Epoch: 843 | Loss: 9.116436004638672 
Epoch: 844 | Loss: 9.114063262939453 
Epoch: 845 | Loss: 9.111702919006348 
Epoch: 846 | Loss: 9.109345436096191 
Epoch: 847 | Loss: 9.106966972351074 
Epoch: 848 | Loss: 9.104599952697754 
Epoch: 849 | Loss: 9.102245330810547 
Epoch: 850 | Loss: 9.099886894226074 
Epoch: 851 | Loss: 9.097529411315918 
Epoch: 852 | Loss: 9.095175743103027 
Epoch: 853 | Loss: 9.092818260192871 
Epoch: 854 | Loss: 9.090465545654297 
Epoch: 855 | Loss: 9.088120460510254 
Epoch: 856 | Loss: 9.085769653320312 
Epoch: 857 | Loss: 9.08342170715332 
Epoch: 858 | Loss: 9.081079483032227 
Epoch: 859 | Loss: 9.0787353515625 
Epoch: 860 | Loss: 9.076388359069824 
Epoch: 861 | Loss: 9.074060440063477 
Epoch: 862 | Loss: 9.0717191696167 
Epoch: 863 | Loss: 9.069387435913086 
Epoch: 864 | Loss: 9.067063331604004 
Epoch: 865 | Loss: 9.06472110748291 
Epoch: 866 | Loss: 9.06240463256836 
Epoch: 867 | Loss: 9.060052871704102 
Epoch: 868 | Loss: 9.057743072509766 
Epoch: 869 | Loss: 9.055414199829102 
Epoch: 870 | Loss: 9.053094863891602 
Epoch: 871 | Loss: 9.050772666931152 
Epoch: 872 | Loss: 9.048469543457031 
Epoch: 873 | Loss: 9.04615592956543 
Epoch: 874 | Loss: 9.043828010559082 
Epoch: 875 | Loss: 9.041522979736328 
Epoch: 876 | Loss: 9.039206504821777 
Epoch: 877 | Loss: 9.036898612976074 
Epoch: 878 | Loss: 9.034595489501953 
Epoch: 879 | Loss: 9.032292366027832 
Epoch: 880 | Loss: 9.029991149902344 
Epoch: 881 | Loss: 9.027688026428223 
Epoch: 882 | Loss: 9.02540111541748 
Epoch: 883 | Loss: 9.023104667663574 
Epoch: 884 | Loss: 9.020820617675781 
Epoch: 885 | Loss: 9.018515586853027 
Epoch: 886 | Loss: 9.016229629516602 
Epoch: 887 | Loss: 9.013932228088379 
Epoch: 888 | Loss: 9.011646270751953 
Epoch: 889 | Loss: 9.009364128112793 
Epoch: 890 | Loss: 9.007074356079102 
Epoch: 891 | Loss: 9.004809379577637 
Epoch: 892 | Loss: 9.00251579284668 
Epoch: 893 | Loss: 9.000255584716797 
Epoch: 894 | Loss: 8.997966766357422 
Epoch: 895 | Loss: 8.995702743530273 
Epoch: 896 | Loss: 8.993427276611328 
Epoch: 897 | Loss: 8.991157531738281 
Epoch: 898 | Loss: 8.988892555236816 
Epoch: 899 | Loss: 8.986623764038086 
Epoch: 900 | Loss: 8.984360694885254 
Epoch: 901 | Loss: 8.982105255126953 
Epoch: 902 | Loss: 8.979848861694336 
Epoch: 903 | Loss: 8.977577209472656 
Epoch: 904 | Loss: 8.975320816040039 
Epoch: 905 | Loss: 8.973063468933105 
Epoch: 906 | Loss: 8.970806121826172 
Epoch: 907 | Loss: 8.968571662902832 
Epoch: 908 | Loss: 8.96631145477295 
Epoch: 909 | Loss: 8.964072227478027 
Epoch: 910 | Loss: 8.961827278137207 
Epoch: 911 | Loss: 8.959582328796387 
Epoch: 912 | Loss: 8.957332611083984 
Epoch: 913 | Loss: 8.955102920532227 
Epoch: 914 | Loss: 8.952855110168457 
Epoch: 915 | Loss: 8.950630187988281 
Epoch: 916 | Loss: 8.948387145996094 
Epoch: 917 | Loss: 8.946157455444336 
Epoch: 918 | Loss: 8.943930625915527 
Epoch: 919 | Loss: 8.941699981689453 
Epoch: 920 | Loss: 8.939471244812012 
Epoch: 921 | Loss: 8.937251091003418 
Epoch: 922 | Loss: 8.935022354125977 
Epoch: 923 | Loss: 8.932807922363281 
Epoch: 924 | Loss: 8.93059253692627 
Epoch: 925 | Loss: 8.928369522094727 
Epoch: 926 | Loss: 8.926153182983398 
Epoch: 927 | Loss: 8.923932075500488 
Epoch: 928 | Loss: 8.921730041503906 
Epoch: 929 | Loss: 8.91952133178711 
Epoch: 930 | Loss: 8.917296409606934 
Epoch: 931 | Loss: 8.915095329284668 
Epoch: 932 | Loss: 8.912897109985352 
Epoch: 933 | Loss: 8.91069221496582 
Epoch: 934 | Loss: 8.908493995666504 
Epoch: 935 | Loss: 8.90629768371582 
Epoch: 936 | Loss: 8.904097557067871 
Epoch: 937 | Loss: 8.901898384094238 
Epoch: 938 | Loss: 8.899701118469238 
Epoch: 939 | Loss: 8.89752197265625 
Epoch: 940 | Loss: 8.895334243774414 
Epoch: 941 | Loss: 8.893135070800781 
Epoch: 942 | Loss: 8.89094352722168 
Epoch: 943 | Loss: 8.888771057128906 
Epoch: 944 | Loss: 8.886575698852539 
Epoch: 945 | Loss: 8.88440227508545 
Epoch: 946 | Loss: 8.88222599029541 
Epoch: 947 | Loss: 8.880043983459473 
Epoch: 948 | Loss: 8.877878189086914 
Epoch: 949 | Loss: 8.875691413879395 
Epoch: 950 | Loss: 8.87352180480957 
Epoch: 951 | Loss: 8.871352195739746 
Epoch: 952 | Loss: 8.869190216064453 
Epoch: 953 | Loss: 8.867023468017578 
Epoch: 954 | Loss: 8.864850044250488 
Epoch: 955 | Loss: 8.862689971923828 
Epoch: 956 | Loss: 8.8605318069458 
Epoch: 957 | Loss: 8.858368873596191 
Epoch: 958 | Loss: 8.856209754943848 
Epoch: 959 | Loss: 8.854063987731934 
Epoch: 960 | Loss: 8.851890563964844 
Epoch: 961 | Loss: 8.849754333496094 
Epoch: 962 | Loss: 8.847596168518066 
Epoch: 963 | Loss: 8.84544563293457 
Epoch: 964 | Loss: 8.843304634094238 
Epoch: 965 | Loss: 8.841158866882324 
Epoch: 966 | Loss: 8.839015007019043 
Epoch: 967 | Loss: 8.83687973022461 
Epoch: 968 | Loss: 8.83473014831543 
Epoch: 969 | Loss: 8.832598686218262 
Epoch: 970 | Loss: 8.830455780029297 
Epoch: 971 | Loss: 8.828330039978027 
Epoch: 972 | Loss: 8.826186180114746 
Epoch: 973 | Loss: 8.82406997680664 
Epoch: 974 | Loss: 8.821927070617676 
Epoch: 975 | Loss: 8.819806098937988 
Epoch: 976 | Loss: 8.817682266235352 
Epoch: 977 | Loss: 8.815550804138184 
Epoch: 978 | Loss: 8.813434600830078 
Epoch: 979 | Loss: 8.811302185058594 
Epoch: 980 | Loss: 8.809192657470703 
Epoch: 981 | Loss: 8.807075500488281 
Epoch: 982 | Loss: 8.804969787597656 
Epoch: 983 | Loss: 8.802851676940918 
Epoch: 984 | Loss: 8.80074691772461 
Epoch: 985 | Loss: 8.798626899719238 
Epoch: 986 | Loss: 8.796518325805664 
Epoch: 987 | Loss: 8.794412612915039 
Epoch: 988 | Loss: 8.792304992675781 
Epoch: 989 | Loss: 8.790201187133789 
Epoch: 990 | Loss: 8.788098335266113 
Epoch: 991 | Loss: 8.785994529724121 
Epoch: 992 | Loss: 8.783905982971191 
Epoch: 993 | Loss: 8.781818389892578 
Epoch: 994 | Loss: 8.779707908630371 
Epoch: 995 | Loss: 8.77762222290039 
Epoch: 996 | Loss: 8.775525093078613 
Epoch: 997 | Loss: 8.77344036102295 
Epoch: 998 | Loss: 8.771352767944336 
Epoch: 999 | Loss: 8.769270896911621 
