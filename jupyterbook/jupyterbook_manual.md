# jupyter-book manual

## 새로운 페이지를 추가할 때
1. jupyterbook/ 폴더 아래에 새로 파일을 만든다.
2. jupyterbook/_toc.yml 에 추가된 파일 이름을 넣는다. (확장자는 없어도 되지만 헷갈리니까 넣자.)

```yaml
chapters:
- file: {기존 파일들}
- file: new_notebook.ipynb
```
3. `jb build jupyterbook/`을 실행한다.
4. 로컬에서 완성된 html을 확인한다.

### 작성 중 팁
- 빌드는 신중하게 하자. build할 때마다 노트북을 실행시키기 떄문에 git diff가 생겨버린다.
- commit 하기 전에 빌드를 해놓자.

## Publish
- 미리 ghp-import를 깔아놓는다.
```shell
pip install ghp-import
```
1. 빌드 후 잘 완성됐는지 확인한다.
2. jupyterbook/ 위치로 이동해서 다음을 터미널에 실행한다.
```shell
ghp-import -n -p -f _build/html
```
3. main 브랜치의 내용이 gh-pages 브랜치에 복사된다.
