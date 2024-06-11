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

## 